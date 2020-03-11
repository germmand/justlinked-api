import os
import requests

from fastapi import APIRouter
from starlette.responses import RedirectResponse

from .google_oauth import GoogleOAuth2
from .service import GoogleApplicantService

from src.core.config.config import Config
from src.core.config.session import db_session

router = APIRouter()
redirect_uri = Config.HOST + '/login/google/callback'
google_auth = GoogleOAuth2(os.environ["GOOGLE_CLIENT_ID"],
                           os.environ["GOOGLE_CLIENT_SECRET"],
                           requests,
                           redirect_uri)
google_applicant_service = GoogleApplicantService(db_session)

@router.get("/login/google", tags=["external_login"])
async def get_google_auth_server_url():
    google_auth_server_url = google_auth.assemble_auth_server_url()
    response = RedirectResponse(url=google_auth_server_url)
    return response

@router.get('/login/google/callback', tags=["external_login_callback"])
async def handle_google_login_response(code = None, error = None):
    if error is not None:
        return {'error': error}
    google_tokens_response = google_auth.get_tokens(code)
    access_token = google_tokens_response.json()["access_token"]
    google_user_data = google_auth.get_user_data(access_token, ['names', 'addresses', 'residences', 'emailAddresses', 'birthdays', 'photos'])
    applicant = google_applicant_service.obtain_applicant(google_user_data.json())
    return { 'email': applicant.email, 'success': True }