import logging
from typing import Dict

from .config import HandlerConfig
from ...factory import ObjectFactory

__all__ = ['get_handler', 'get_handler_config', 'handler_factory', 'handler_config_factory']

handler_factory = ObjectFactory(logging.Handler)
handler_config_factory = ObjectFactory(HandlerConfig)


def get_handler(handler: str, handler_config: Dict = None) -> logging.Handler:
    config = get_handler_config(handler, handler_config)
    return handler_factory.get(handler)(config)


def get_handler_config(handler: str, handler_config: Dict = None):
    if handler_config is None:
        handler_config = dict()
    config = handler_config_factory.get(handler).from_dict(handler_config)
    return config
