from urllib.parse import urlencode

def create_google_auth_server_url(client_id, redirect_uri, scopes):
    url = 'https://accounts.google.com/o/oauth2/v2/auth'
    params = {
        'client_id': client_id,
        'access_type': 'offline',
        'response_type': 'code',
        'include_granted_scopes': 'true',
        'redirect_uri': redirect_uri,
        'scope': ' '.join(scopes)
    }
    params = urlencode(params)
    return '{}?{}'.format(url, params)