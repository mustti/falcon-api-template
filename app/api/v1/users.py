from sqlalchemy.exc import DBAPIError

from falcon.media.validators.jsonschema import validate

from app.api.common import BaseResource
from app.model import user
from app.utils import password




class Collection(BaseResource):

    user_validator = {
        "title": "User",
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": "Username"
            },
            "password": {
                "type": "string",
                "description": "User's password"
            }
        },
        "required": ["username", "password"]
    }

    @validate(user_validator)
    def on_post(self, req, resp):
        
        session = req.context['session']

        media = req.media

        user_schema = user.UserSchema()

        user_db = session.query(user.User) \
            .filter(user.User.username == media['username']) \
            .first()

        if user_db:
            self.on_duplicate("User already registered.", resp)

            
        media['password'] = password.encrypt_password(media['password'])

        user_data = user_schema.load(media, session=session).data

        session.add(user_data)


    def on_get(self, req, resp):
        
        session = req.context['session']

        user_db = session.query(user.User).all()
        
        user_schema = user.UserSchema()

        data = user_schema.dump(user_db, many=True).data

        resp.media = data

class Item(BaseResource):

    def __init__(self):
        return

    def on_get(self, req, resp):
        return
