from dataclasses import dataclass, field
from typing import List, Iterable

from .component import ComponentState
from .io_component import IOComponent, IOComponentConfig
from ...stream import InputStream, OutputStream

__all__ = ['BatchComponent', 'BatchComponentConfig', 'BatchComponentState']


@dataclass
class BatchComponentConfig(IOComponentConfig):
    name: str = 'batch_component_config'
    batch_size: int = 1


@dataclass
class BatchComponentState(ComponentState):
    batch: List = field(default_factory=list)


class BatchComponent(IOComponent):
    def __init__(self, config: BatchComponentConfig, input_stream: InputStream, output_stream: OutputStream):
        super(BatchComponent, self).__init__(config, input_stream, output_stream)

    def init_state(self) -> BatchComponentState:
        return BatchComponentState()

    @property
    def current_batch(self):
        return self.state.batch

    @property
    def batch_size(self):
        return self.config.batch_size

    def preprocess(self, data):
        self.add_to_batch(data)
        if self.batch_is_ready():
            return self.current_batch
        else:
            return []

    def process(self, batch: List) -> Iterable:
        raise NotImplementedError

    def after_process(self, data):
        if self.batch_is_ready():
            self.reset_batch()

    def on_end_of_stream(self, data):
        if len(self.current_batch) > 0:
            self.batch_lifecycle(self.current_batch)
            self.reset_batch()

    def add_to_batch(self, data):
        self.current_batch.append(data)

    def batch_is_ready(self):
        return len(self.current_batch) == self.batch_size

    def reset_batch(self):
        self.state.batch = list()

    def send_output(self, outputs):
        for output in outputs:
            self.output_stream.send(output)

    def batch_lifecycle(self, batch):
        output = self.process(batch)
        self.after_process(output)
        postprocessed_output = self.postprocess(output)
        self.after_postprocess(postprocessed_output)
        self.send_output(postprocessed_output)
