import logging
import sys
from dataclasses import dataclass
from enum import IntEnum

from .config import HandlerConfig
from .factory import handler_factory, handler_config_factory

__all__ = ['Standard', 'StandardHandlerConfig', 'StandardHandler']


class Standard(IntEnum):
    OUT = 0
    ERR = 1


@handler_config_factory.register('std')
@dataclass
class StandardHandlerConfig(HandlerConfig):
    stream: Standard = Standard.OUT


@handler_factory.register('std')
class StandardHandler(logging.StreamHandler):
    def __init__(self, config: StandardHandlerConfig):
        stream = self.get_stream(config.stream)
        super(StandardHandler, self).__init__(stream)

    @staticmethod
    def get_stream(stream: Standard):
        if stream == Standard.OUT:
            return sys.stdout
        else:
            return sys.stderr
