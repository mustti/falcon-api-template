from app.api.common import BaseResource
from app.model import user
from falcon.media.validators.jsonschema import validate
from app.utils import password, token

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

        # search a user bu its username
        user_db = session.query(user.User) \
            .filter(user.User.username == media['username']) \
            .first()
        
        if not user_db:
            self.on_not_found("User not found", resp)

        # serialize the response
        user_data = user_schema.dump(user_db).data

        if password.check_password(media['password'], user_data['password']):
            
            decoded_token = token.encode_token({'iss': user_data['id']})

            self.on_created({"token": decoded_token}, resp)


        else:
            self.on_unauthorized({"response": "Incorrect user or password."}, resp)
