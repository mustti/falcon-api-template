import bcrypt

def encrypt_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()) \
        .decode('utf-8')

def check_password(input_password: str, password: str) -> bool:
        input_password = input_password.encode('utf-8')
        password = password.encode('utf-8')

        return bcrypt.checkpw(input_password, password)