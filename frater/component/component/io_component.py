from dataclasses import dataclass

from .component import Component, ComponentConfig
from ...stream import InputStream, OutputStream

__all__ = ['IOComponent', 'IOComponentConfig']


@dataclass
class IOComponentConfig(ComponentConfig):
    name: str = 'io_component_config'


class IOComponent(Component):
    def __init__(self, config: IOComponentConfig, input_stream: InputStream, output_stream: OutputStream):
        super(IOComponent, self).__init__(config)
        self.input_stream = input_stream
        self.output_stream = output_stream

    @property
    def _input_stream(self):
        return self.input_stream

    def process(self, data):
        raise NotImplementedError

    def send_output(self, data):
        self.output_stream.send(data)
