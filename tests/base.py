import sys
sys.path.append("..")

from falcon import testing
from app.main import app

class MyTestCase(testing.TestCase):
    def setUp(self):
        super(MyTestCase, self).setUp()

        self.app = main.app


class TestMyApp(MyTestCase):
    def test_status(self):
        response = 'Everything is fine!'

        result = self.simulate_get('/v1/status')
        self.assertEqual(result.json, response)
        
