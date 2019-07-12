from frater.core import Activity
from frater.core.activity import ActivityProposal
from frater.stream import InputStream, OutputStream
from frater.task import IOTask


class ActivityClassifier(IOTask):
    def __init__(self, input_stream: InputStream, output_stream: OutputStream):
        super(ActivityClassifier, self).__init__(input_stream, output_stream)

    def perform_task(self, proposal: ActivityProposal) -> Activity:
        raise NotImplementedError