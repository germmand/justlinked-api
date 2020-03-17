from urllib.parse import urlencode

class GoogleOAuth2(object):
    SCOPES = ['https://www.googleapis.com/auth/contacts.readonly', 
              'https://www.googleapis.com/auth/user.addresses.read',
              'https://www.googleapis.com/auth/user.birthday.read',
              'https://www.googleapis.com/auth/user.emails.read',
              'https://www.googleapis.com/auth/user.organization.read',
              'https://www.googleapis.com/auth/user.phonenumbers.read',
              'https://www.googleapis.com/auth/userinfo.email',
              'https://www.googleapis.com/auth/userinfo.profile']

    def __init__(self, client_id, client_secret, http):
        self.client_id = client_id
        self.client_secret = client_secret
        self.http = http

    def assemble_auth_server_url(self, redirect_uri):
        url = 'https://accounts.google.com/o/oauth2/v2/auth'
        params = {
            'client_id': self.client_id,
            'access_type': 'offline',
            'response_type': 'code',
            'include_granted_scopes': 'true',
            'redirect_uri': redirect_uri,
            'scope': ' '.join(self.SCOPES)
        }
        params = urlencode(params)
        return '{}?{}'.format(url, params)

    def get_tokens(self, code, redirect_uri):
        url = 'https://oauth2.googleapis.com/token'
        params = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': redirect_uri
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        google_tokens_response = self.http.post(url=url, data=params, headers=headers)
        return google_tokens_response

    def get_user_data(self, access_token, fields):
        fields_comma_separated = ','.join(fields)
        url = 'https://people.googleapis.com/v1/people/me?personFields={}'.format(fields_comma_separated)
        headers = {
            'Authorization': 'Bearer {}'.format(access_token)
        }
        google_user_data = self.http.get(url=url, headers=headers)
        return google_user_data