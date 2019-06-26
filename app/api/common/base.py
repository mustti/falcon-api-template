import falcon
from falcon import Response, Request

class BaseResource:
    def __init__(self):
        return

    @staticmethod
    def on_success(data, response):
        meta = {
                "code": falcon.HTTP_200
        }

        value = {
            "meta": meta,
            "response": data
        }

        response.media = value
        response.code = falcon.HTTP_200

    @staticmethod
    def on_error(data, response):
        meta = {
                "code": falcon.HTTP_500
        }

        value = {
            "meta": meta,
            "response": data
        }

        response.media = value
        response.code = falcon.HTTP_500

    @staticmethod
    def on_duplicate(data, response):
        meta = {
                "code": falcon.HTTP_409
        }

        value = {
            "meta": meta,
            "response": data
        }

        response.media = value
        response.code = falcon.HTTP_409

    @staticmethod
    def on_not_found(data, response):
        meta = {
                "code": falcon.HTTP_404
        }

        value = {
            "meta": meta,
            "response": data
        }

        response.media = value
        response.code = falcon.HTTP_404

    @staticmethod
    def on_unauthorized(data, response):
        meta = {
                "code": falcon.HTTP_403
        }

        value = {
            "meta": meta,
            "response": data
        }

        response.media = value
        response.code = falcon.HTTP_404

    @staticmethod
    def on_created(data, response):
        meta = {
                "code": falcon.HTTP_201
        }

        value = {
            "meta": meta,
            "response": data
        }

        response.media = value
        response.code = falcon.HTTP_201
