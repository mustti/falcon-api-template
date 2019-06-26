from sqlalchemy import Column
from sqlalchemy import DateTime, func
from sqlalchemy.ext.declarative import declarative_base, declared_attr


class BaseModel(object):
    created = Column(DateTime, default=func.now())
    modified = Column(DateTime, default=func.now(), onupdate=func.now())

    @declared_attr
    def __tablename__(self):
        return self.__name__.lower()


Base = declarative_base(cls=BaseModel)