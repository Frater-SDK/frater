from .task import Task
from ..stream import InputStream, OutputStream
from ..utilities.task import is_end_of_sequence


class IOTask(Task):
    def __init__(self, input_stream: InputStream, output_stream: OutputStream):
        super(IOTask, self).__init__()
        self._input_stream = input_stream
        self._output_stream = output_stream

    @property
    def input_stream(self):
        return self._input_stream

    @property
    def output_stream(self):
        return self._output_stream

    def run(self):
        for data in self.input_stream:
            if is_end_of_sequence(data):
                self._active = False
                self.output_stream(data)
            else:
                self._active = True
                output = self.perform_task(data)
                self.output_stream(output)

    def perform_task(self, data):
        raise NotImplementedError

    def stop(self):
        self.input_stream.close()
        self.output_stream.close()
        super(IOTask, self).stop()
