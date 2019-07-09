from typing import Iterator

from frater.core import ActivityProposal, Object
from frater.task import IOTask
from frater.utilities.stream import StreamState


class ActivityProposer(IOTask):
    def __init__(self, input_stream, output_stream):
        super(ActivityProposer, self).__init__(input_stream, output_stream)

    def perform_task(self, object: Object) -> Iterator[ActivityProposal]:
        """
        This should take in a stream of objects and yield Activity Proposals from an iterator
        :param object:
        :return:
        """
        raise NotImplementedError

    def run(self):
        for data in self.input_stream:
            if type(data) is StreamState and data == StreamState.EOS:
                self._active = False
                self.output_stream(data)
            else:
                self._active = True
                for proposal in self.perform_task(data):
                    self.output_stream(proposal)
