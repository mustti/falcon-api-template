from app.model import BaseModel
from sqlalchemy import Column, ForeignKey
from sqlalchemy import String, Integer, Text, Boolean, UniqueConstraint

from marshmallow_sqlalchemy import ModelSchema

class User(BaseModel):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(Text, nullable=False, unique=True)
    password = Column(Text, nullable=False)
    UniqueConstraint('username')

    def __repr__(self):
        return "<User(id='%s', username='%s', password='%s')>" % (self.id, self.username, self.password)

    @classmethod
    def get_id(cls):
        return User.user_id

class UserSchema(ModelSchema):
    class Meta:
        model = User