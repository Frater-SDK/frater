from .task import Task
from ..stream import InputStream


class InputTask(Task):
    def __init__(self, input_stream: InputStream):
        super(InputTask, self).__init__()
        self._input_stream = input_stream

    @property
    def input_stream(self):
        return self._input_stream

    def run(self):
        for data in self.input_stream:
            if self.stopped:
                break
            self.perform_task(data)

    def stop(self):
        self.input_stream.close()
        super(InputTask, self).stop()

    def perform_task(self, data):
        raise NotImplementedError
