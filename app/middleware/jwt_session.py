import falcon
from falcon import Request, Response
from jwt.exceptions import DecodeError, ExpiredSignatureError

from app.api.common import BaseResource
from app.utils import token

class JWTSessionManager(BaseResource):
    def __init__(self):
        self._ignore_paths = ['/v1/session', '/v1/status']

    def process_request(self, req: Request, resp: Response, *args):
        if req.path in self._ignore_paths:
            pass
        else:
            
            headers = req.headers
            
            if not 'AUTHORIZATION' in headers:
                raise falcon.HTTPUnauthorized(title='Token not found', description="Token required")

            header_token = headers['AUTHORIZATION']

            try:
                header_token = token.decode_token(header_token)  
            except DecodeError:
                raise falcon.HTTPUnauthorized(title='Invalid token', description='Invalid token')
            except ExpiredSignatureError:
                raise falcon.HTTPUnauthorized(title='Expired token', description='Your session is expired')