from src.auth.jwt_manager import JwtManager
from src.core.config.config import Config

# This is the one that has to be used when either encoding or decoding tokens.
# The reason for this is because the idea behind it is to share an instance with the same configuration
# across the whole application.
JWTManager = JwtManager(issuer=Config.HOST, 
                        audience=Config.WEBCLIENT_HOST, 
                        secret=Config.JWT_SECRET)