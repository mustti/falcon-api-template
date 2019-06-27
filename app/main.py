import falcon

# Middleware
from app.middleware import DatabaseSessionManager, JWTSessionManager

from app.api.v1 import users, session, status

app = falcon.API(middleware=[DatabaseSessionManager(), JWTSessionManager()])

app.add_route('/v1/users', users.Collection())

app.add_route('/v1/session', session.Collection())

app.add_route('/v1/status', status.Collection())

if __name__ == 'app.main':

    from app.database import session, engine
    
    session.configure(bind=engine)

    from app.model import BaseModel
    BaseModel.metadata.create_all(engine)