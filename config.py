import os
from pathlib import Path

JWT_SECRET = os.getenv('JWT_SECRET', '123')
JWT_ALGORITHM = 'HS256'

# expiration in minutes
JWT_EXP = (1400) * 60


DATABASE_DIR = Path(os.path.dirname(__file__)) / 'bin' / 'database'
DATABASE_URL = 'sqlite:///%s/sqlite3.db' % (DATABASE_DIR)
DATABASE_ECHO = False