import os
from pathlib import Path

# expiration in minutes
JWT_EXP = (1400) * 60
JWT_SECRET = os.getenv('JWT_SECRET', '123')
JWT_ALGORITHM = 'HS256'


DATABASE_DIR = Path(os.path.dirname(__file__)) / 'bin' / 'database'
DATABASE_URL = 'sqlite:///%s/sqlite3.db' % (DATABASE_DIR)
DATABASE_ECHO = False
if not os.path.exists(DATABASE_DIR):
    os.makedirs(DATABASE_DIR)
