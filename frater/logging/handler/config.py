import logging
from dataclasses import dataclass

from frater.config import Config


@dataclass
class HandlerConfig(Config):
    name: str = 'handler_config'
    level: int = logging.INFO
