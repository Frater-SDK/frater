import inspect
from typing import Callable


def has_argument(handler: Callable, argument: str):
    return argument in inspect.getfullargspec(handler).args
