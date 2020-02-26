import logging
from dataclasses import field, dataclass

from .handler.factory import get_handler
from ..config import Config


@dataclass
class LoggerConfig(Config):
    name: str = field(default=__name__)
    handler: str = 'stdout'
    format: str = '%(asctime)s | %(name)s | %(levelname)s | %(message)s'
    level: int = logging.INFO


def get_logger(config: LoggerConfig) -> logging.Logger:
    handler = get_handler(config.handler)
    formatter = logging.Formatter(config.format)
    handler.setFormatter(formatter)

    logger = logging.getLogger(config.name)
    logger.addHandler(handler)
    logger.setLevel(config.level)

    return logger
