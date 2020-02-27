from unittest.mock import Mock

import flask

from frater.server.middleware import *


def get_mock_func():
    mock_func = Mock()
    mock_func.return_value = {'test': 1234}

    return mock_func


def get_app():
    return flask.Flask(__name__)


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
    reduced = reduce_middleware([mock_middleware])
    assert reduced(mock_func)() == {'test': 1234, 'other': 1}

    mock_func.reset_mock()
    app = get_app()
    middleware = [mock_middleware, response_middleware]
    with app.test_request_context():
        reduced = reduce_middleware(middleware)
        res = reduced(mock_func)()
        assert res.json == {'test': 1234, 'other': 1}
        assert res.status_code == 200


def test_response_middleware():
    mock_func = get_mock_func()
    app = get_app()
    with app.test_request_context():
        res = response_middleware(mock_func)()
        assert res.json == {'test': 1234}
        assert res.status_code == 200


def test_identity_middleware():
    mock_func = get_mock_func()
    wrapper = identity_middleware(mock_func)

    assert wrapper() == mock_func()


def test_get_default_middleware():
    middleware = get_default_middleware()

    mock_func = get_mock_func()

    app = get_app()
    with app.test_request_context():
        res = middleware(mock_func)()
        assert res.json == {'test': 1234}
        assert res.status_code == 200
