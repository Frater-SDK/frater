from dataclasses import dataclass, field
from typing import Callable, List

from dataclasses_json import DataClassJsonMixin


@dataclass
class Handler(DataClassJsonMixin):
    """
    :param endpoint: API endpoint for handler func
    :param name: Flask view function name
    :param func: handler function
    :param methods: HTTP methods for handler function
    """
    endpoint: str
    name: str
    func: Callable
    methods: List[str] = field(default_factory=lambda: ['GET'])

    def to_dict(self, **kwargs):
        return {'endpoint': self.endpoint, 'name': self.name, 'methods': self.methods}
