from dataclasses import dataclass

from .component import Component, ComponentConfig
from ...stream import OutputStream

__all__ = ['OutputComponent', 'OutputComponentConfig']


@dataclass
class OutputComponentConfig(ComponentConfig):
    name: str = 'output_component_config'


class OutputComponent(Component):
    def __init__(self, config: ComponentConfig, output_stream: OutputStream):
        super(OutputComponent, self).__init__(config)
        self.output_stream = output_stream

    @property
    def _input_stream(self):
        return self.generate()

    def generate(self):
        raise NotImplementedError

    def process(self, data):
        raise NotImplementedError

    def send_output(self, output):
        self.output_stream.send(output)
