from functools import wraps
from graphql import GraphQLError
from src.auth import JWTManager
from src.auth.models.authenticated_user import AuthenticatedUser

def _extract_access_token_from_request(request):
    auth_header = request.headers.get('Authorization', None)
    if auth_header is None:
        raise GraphQLError('No authorization provided')
    token_type, access_token = auth_header.split(' ')
    return token_type, access_token

def _verify_token_type(decoded_token, expected_type):
    if decoded_token['type'] != expected_type:
        raise GraphQLError('Token type not supported')

def jwt_required(fn):
    @wraps(fn)
    def wrapper(parent, info, **kwargs):
        request = info.context["request"]
        token_type, access_token = _extract_access_token_from_request(request)
        decoded_token = JWTManager.decode_jwt(access_token)
        _verify_token_type(decoded_token, token_type)
        user_claims = decoded_token[JWTManager.user_claims_key]
        info.context['user'] = AuthenticatedUser(**user_claims)
        return fn(parent, info, **kwargs)
    return wrapper