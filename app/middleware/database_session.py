from falcon import Request, Response
from sqlalchemy.exc import SQLAlchemyError

from app.database import session as db_session


class DatabaseSessionManager:
    def process_request(self, request: Request, response: Response, *args):
        request.context['session'] = db_session

    def process_response(self, request: Request, response: Response, *args):
        
        session = request.context['session']

        try:
            session.commit()
        except SQLAlchemyError as ex:
            print(ex)
            session.rollback()
        finally:
            session.close()
        