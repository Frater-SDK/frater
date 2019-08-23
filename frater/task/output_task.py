from .task import Task
from ..stream import OutputStream


class OutputTask(Task):
    def __init__(self, output_stream: OutputStream):
        super(OutputTask, self).__init__()
        self._output_stream = output_stream

    @property
    def output_stream(self):
        return self._output_stream

    def run(self):
        while self.run_condition() and not self._stopped:
            output = self.perform_task()
            self.output_stream(output)

    def perform_task(self, **kwargs):
        raise NotImplementedError

    def run_condition(self) -> bool:
        raise NotImplementedError

    def stop(self):
        self.output_stream.close()
        super(OutputTask, self).stop()
