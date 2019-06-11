from typing import Generator

from frater.core import ActivityProposal, Object
from frater.task import IOTask


class ActivityProposer(IOTask):
    def __init__(self, input_stream, output_stream):
        super(ActivityProposer, self).__init__(input_stream, output_stream)

    def perform_task(self, object: Object) -> Generator[ActivityProposal]:
        """
        This should take in a stream of objects and yield Activity Proposals from a generator
        :param object:
        :return:
        """

    def run(self):
        for object in self.input_stream:
            for proposal in self.perform_task(object):
                self.output_stream(proposal)
