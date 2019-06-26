import time
import jwt
import config

def encode_token(payload: dict) -> str:
    current_time = int(time.time())
    
    payload['iat'] = current_time
    payload['exp'] = current_time + config.JWT_EXP
    
    return jwt.encode(payload, config.JWT_SECRET, algorithm=config.JWT_ALGORITHM).decode('utf-8')

def decode_token(token: str) -> dict:
    token = token.encode('utf-8')
    return jwt.decode(token, config.JWT_SECRET, algorithms=[config.JWT_ALGORITHM])