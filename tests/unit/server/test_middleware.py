from unittest.mock import patch, Mock

import flask

from frater.server.middleware import *


def get_mock_func():
    mock_func = Mock()
    mock_func.return_value = {'test': 1234}

    return mock_func


def get_context():
    return flask.Flask(__name__).app_context()


def mock_middleware(handler):
    def wrapper():
        res = handler()
        res['other'] = 1
        return res

    return wrapper


def test_reduce_middleware():
    middleware = []
    reduced = reduce_middleware(middleware)

    mock_func = get_mock_func()

    assert reduced(mock_func)() == mock_func()

    mock_func.reset_mock()

    ctx = get_context()
    with ctx:
        with patch('frater.server.middleware.request') as request:
            middleware = [mock_middleware, response_middleware]
            reduced = reduce_middleware(middleware)
            request.method.return_value = 'GET'
            res = reduced(mock_func)()
            assert res.json == {'test': 1234, 'other': 1}
            assert res.status_code == 200

    mock_func.reset_mock()

    reduced = reduce_middleware([mock_middleware])

    assert reduced(mock_func)() == {'test': 1234, 'other': 1}


def test_response_middleware():
    mock_func = get_mock_func()
    ctx = get_context()

    with ctx:
        with patch('frater.server.middleware.request') as request:
            request.method.return_value = 'GET'
            func = response_middleware(mock_func)
            assert func().json == {"test": 1234}
            assert func().status_code == 200


def test_identity_middleware():
    mock_func = get_mock_func()
    wrapper = identity_middleware(mock_func)

    assert wrapper() == mock_func()


def test_get_default_middleware():
    middleware = get_default_middleware()

    mock_func = get_mock_func()
    ctx = get_context()

    with ctx:
        with patch('frater.server.middleware.request') as request:
            request.method.return_value = 'GET'
            func = middleware(mock_func)
            assert func().json == {"test": 1234}
            assert func().status_code == 200
