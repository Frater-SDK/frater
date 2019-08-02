from dataclasses import dataclass, field
from typing import List

from frater.core import Activity, ActivityProposal, Modality
from frater.stream import InputStream, OutputStream
from frater.task import IOTask
from frater.utilities.stream import StreamState


@dataclass
class ActivityClassifierConfig:
    classifier_name: str = ''
    weights: str = ''
    num_categories: int = 0
    batch_size: int = 1
    modality: str = field(default='RGB')
    gpus: List[int] = field(default_factory=list)

    @property
    def modality_type(self) -> Modality:
        return Modality[self.modality]


class ActivityClassifier(IOTask):
    def __init__(self, input_stream: InputStream, output_stream: OutputStream, config: ActivityClassifierConfig):
        super(ActivityClassifier, self).__init__(input_stream, output_stream)
        self.config = config
        self.current_batch: List[ActivityProposal] = list()

    @property
    def batch_size(self):
        return self.config.batch_size

    def perform_task(self, proposals: List[ActivityProposal]) -> List[Activity]:
        raise NotImplementedError

    def run(self):
        for data in self.input_stream:
            if type(data) is StreamState and data == StreamState.EOS:
                outputs = self.perform_task(self.current_batch)
                for output in outputs:
                    self.output_stream(output)
                self.reset_batch()

                self._active = False
                self.output_stream(data)
            else:
                self._active = True
                self.add_to_batch(data)
                if self.batch_is_ready():
                    outputs = self.perform_task(self.current_batch)
                    for output in outputs:
                        self.output_stream(output)
                    self.reset_batch()

    def add_to_batch(self, proposal: ActivityProposal):
        self.current_batch.append(proposal)

    def batch_is_ready(self):
        return len(self.current_batch) == self.batch_size

    def reset_batch(self):
        self.current_batch = list()
