from app.api.common import BaseResource

class Collection(BaseResource):

    def on_get(self, req, resp):
        try:
            session = req.context['session']
            self.on_success("Everything is fine!", resp)
        except:
            self.on_error("I don't feel so good", resp)
        

        