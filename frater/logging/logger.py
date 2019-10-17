import logging
import sys


def get_logger(name='', handler=None, formatter=None, level=logging.INFO):
    if handler is None:
        handler = logging.StreamHandler(sys.stdout)
    if formatter is None:
        formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.addHandler(handler)
    logger.setLevel(level)
    return logger
