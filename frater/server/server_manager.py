from typing import List

from flask import Flask

from ..utilities import Handler

__all__ = ['ServerManager']


class ServerManager:
    def __init__(self, middleware):
        self.server = Flask(__name__)
        self.middleware = middleware

    def get_server(self):
        return self.server

    def add_handler(self, handler: Handler):
        self.server.add_url_rule(handler.endpoint, handler.name, self.middleware(handler.func), methods=handler.methods)

    def register_endpoints(self, handlers: List[Handler]):
        for handler in handlers:
            self.add_handler(handler)
