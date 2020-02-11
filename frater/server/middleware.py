from functools import reduce
from typing import Callable

from flask import request, jsonify

from ..utilities.function import has_argument

__all__ = ['reduce_middleware', 'get_default_middleware', 'response_middleware', 'identity_middleware']


def reduce_middleware(middleware):
    def wrapper_func(handler):
        if len(middleware) == 0:
            return identity_middleware(handler)
        elif len(middleware) == 1:
            return middleware[0](handler)
        else:
            return reduce(lambda f, g: g(f), middleware, handler)

    return wrapper_func


def get_default_middleware():
    return response_middleware


def response_middleware(handler: Callable):
    def wrapper():
        if request.method in {'POST', 'PATCH', 'PUT', 'DELETE'}:
            return jsonify(handler(request.json))
        else:
            if has_argument(handler, 'params'):
                return jsonify(handler(request.args))
            return jsonify(handler())

    return wrapper


def identity_middleware(handler):
    return handler
