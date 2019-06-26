import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref
import config

engine = sa.create_engine(config.DATABASE_URL, echo=config.DATABASE_ECHO)
session = scoped_session(sessionmaker(bind=engine))
