from dataclasses import dataclass

from .component import Component, ComponentConfig
from ...stream import InputStream

__all__ = ['InputComponent', 'InputComponentConfig']


@dataclass
class InputComponentConfig(ComponentConfig):
    name: str = 'input_component_config'


class InputComponent(Component):
    def __init__(self, config: InputComponentConfig, input_stream: InputStream):
        super(InputComponent, self).__init__(config)
        self.input_stream = input_stream

    @property
    def _input_stream(self):
        return self.input_stream

    def process(self, data):
        raise NotImplementedError

    def send_output(self, data):
        pass
