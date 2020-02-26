import json
import unittest

import responses

from frater.client import API


class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.host = 'localhost'
        cls.port = 8080
        cls.protocol = 'http://'
        cls.endpoint = 'test'

    def setUp(self) -> None:
        self.api = API(self.host, self.port, self.protocol)

    @responses.activate
    def test_get(self):
        responses.add(responses.GET, f'{self.protocol}{self.host}:{self.port}/{self.endpoint}', json={'test': 1234})
        res = self.api.get(self.endpoint)

        assert res == {'test': 1234}
        assert len(responses.calls) == 1

    @responses.activate
    def test_post(self):
        def callback(request):
            data = json.loads(request.body)
            name = data['name']
            response = {'message': f'Hello, {name}'}
            return 200, {}, json.dumps(response)

        responses.add_callback(responses.POST, f'{self.protocol}{self.host}:{self.port}/{self.endpoint}',
                               callback=callback)
        res = self.api.post(self.endpoint, {'name': 'john'})

        assert res == {'message': 'Hello, john'}
        assert len(responses.calls) == 1

    def test_delete(self):
        pass

    def test_put(self):
        pass

    def test_patch(self):
        pass
