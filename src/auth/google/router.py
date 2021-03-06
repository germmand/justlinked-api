import os
import requests

from fastapi import APIRouter, HTTPException
from starlette.responses import RedirectResponse

from .google_oauth import GoogleOAuth2
from .service import GoogleApplicantService

from src.core.config.config import Config
from src.core.config.session import db_session
from src.auth import JWTManager

router = APIRouter()
default_redirect_uri = Config.HOST + '/api/v1/login/google/callback'
google_auth = GoogleOAuth2(os.environ["GOOGLE_CLIENT_ID"],
                           os.environ["GOOGLE_CLIENT_SECRET"],
                           requests)
google_applicant_service = GoogleApplicantService(db_session)

@router.get("/login/google", tags=["external_login"])
async def get_google_auth_server_url(redirect_uri=default_redirect_uri):
    google_auth_server_url = google_auth.assemble_auth_server_url(redirect_uri)
    response = RedirectResponse(url=google_auth_server_url)
    return response

@router.get('/login/google/callback', tags=["external_login_callback"])
async def handle_google_login_response(code = None, error = None, redirect_uri=default_redirect_uri):
    if error is not None:
        raise HTTPException(status_code=502, detail=error)
    try:
        google_tokens_response = google_auth.get_tokens(code, redirect_uri)
        access_token = google_tokens_response.json()["access_token"]
        google_user_data = google_auth.get_user_data(access_token, ['names', 'addresses', 'residences', 'emailAddresses', 'birthdays', 'photos'])
    except requests.exceptions.ConnectionError:
        raise HTTPException(status_code=504, detail="A connection timeout ocurred while connecting to the Google APIs.")
    applicant = google_applicant_service.obtain_applicant(google_user_data.json())
    applicant_access_token = JWTManager.encode_access_token(applicant.get_token_claims())
    return {
        'access_token': applicant_access_token,
        'expires_in': 'Never :)'
    }