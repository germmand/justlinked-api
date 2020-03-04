import os
import requests

from fastapi import APIRouter
from starlette.responses import RedirectResponse

from .utils import create_google_auth_server_url

from src.core.config.config import Config

router = APIRouter()

# Esto se tiene que refactorizar cañon pero ya sirve gg

@router.get("/login/google", tags=["external_login"])
async def get_google_auth_server_url():
    redirect_uri = Config.HOST + router.url_path_for('handle_google_login_response')
    client_id = os.environ["GOOGLE_CLIENT_ID"]
    scopes = ['https://www.googleapis.com/auth/contacts.readonly', 
              'https://www.googleapis.com/auth/user.addresses.read',
              'https://www.googleapis.com/auth/user.birthday.read',
              'https://www.googleapis.com/auth/user.emails.read',
              'https://www.googleapis.com/auth/user.organization.read',
              'https://www.googleapis.com/auth/user.phonenumbers.read',
              'https://www.googleapis.com/auth/userinfo.email',
              'https://www.googleapis.com/auth/userinfo.profile']
    google_auth_server_url = create_google_auth_server_url(client_id, redirect_uri, scopes)
    response = RedirectResponse(url=google_auth_server_url)
    return response

@router.get('/login/google/callback', tags=["external_login_callback"])
async def handle_google_login_response(code = None, error = None):
    if error is not None:
        return {'error': error}
    url = 'https://oauth2.googleapis.com/token'
    redirect_uri = Config.HOST + router.url_path_for('handle_google_login_response')
    params = {
        'client_id': os.environ["GOOGLE_CLIENT_ID"],
        'client_secret': os.environ["GOOGLE_CLIENT_SECRET"],
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    google_response = requests.post(url=url, data=params, headers=headers)
    access_token = google_response.json()["access_token"]
    url = 'https://people.googleapis.com/v1/people/me?personFields=emailAddresses,names,photos,nicknames,birthdays'
    headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }
    google_user_data = requests.get(url=url, headers=headers)
    return google_user_data.json()