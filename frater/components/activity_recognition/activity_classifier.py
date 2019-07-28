from typing import List

from frater.core import Activity, ActivityProposal
from frater.stream import InputStream, OutputStream
from frater.task import IOTask
from frater.utilities.stream import StreamState


class ActivityClassifier(IOTask):
    def __init__(self, input_stream: InputStream, output_stream: OutputStream, batch_size: int = 1):
        super(ActivityClassifier, self).__init__(input_stream, output_stream)
        self.batch_size = batch_size
        self.current_batch: List[ActivityProposal] = list()

    def perform_task(self, proposal: List[ActivityProposal]) -> List[Activity]:
        raise NotImplementedError

    def run(self):
        for data in self.input_stream:
            if type(data) is StreamState and data == StreamState.EOS:
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
