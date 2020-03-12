import jwt

class JwtManager(object):
    def __init__(self, issuer, audience, secret):
        self.issuer = issuer
        self.audience = audience
        self.secret = secret
        self._user_claims_key = 'user_claims'

    def encode_access_token(self, user_claims):
        # We add this method instead of calling ___encode_jwt
        # to provide the type of token we're generating, in this case 'access' token.
        # This is done so that maybe in the future if we want to generate another type such as refresh tokens
        # we could provide the type and delegate the rest to __encode_jwt.
        token_data = {
            'type': 'access'
        }
        token_data[self._user_claims_key] = user_claims
        return self.__encode_jwt(token_data)
    
    def __encode_jwt(self, additional_token_data):
        # We don't assign 'exp' property because for the simplicity of this project
        # we don't want the token to expire.
        token_data = {
            'iss': self.issuer,
            'aud': self.audience,
        }
        token_data.update(additional_token_data)
        encoded_token = jwt.encode(token_data, self.secret, algorithm='HS256')
        return encoded_token

    def decode_jwt(self, encoded_token):
        # We make verify_exp = False so that it doesn't verify the expiration time,
        # this is because we don't include the 'exp' property within the token itself
        # because we don't want it to expire.
        options = {
            'verify_exp': False
        }
        data = jwt.decode(encoded_token, self.secret, audience=self.audience, 
                          issuer=self.issuer, algorithms=['HS256'], options=options)
        return data

    @property
    def user_claims_key(self):
        return self._user_claims_key