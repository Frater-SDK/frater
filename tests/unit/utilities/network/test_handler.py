from unittest import TestCase

from frater.utilities import Handler


class TestHandler(TestCase):
    def test_to_dict(self):
        def test_func():
            return 'test'

        handler = Handler(endpoint='/test', name='get_test', func=test_func, methods=['GET'])

        assert handler.to_dict() == {'endpoint': '/test', 'name': 'get_test', 'methods': ['GET']}
        handler = Handler('/test', 'get_test', test_func)

        assert handler.to_dict() == {'endpoint': '/test', 'name': 'get_test', 'methods': ['GET']}
