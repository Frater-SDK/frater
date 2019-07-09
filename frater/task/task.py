import logging
from functools import reduce
from typing import List

from ..stream import InputStream, OutputStream
from ..utilities.stream import StreamState
from ..validation.error import ValidationError
from ..validation.task import is_valid_composition

logger = logging.getLogger()


class Task:
    def __init__(self, input_type=None, output_type=None):
        self._input_type = input_type
        self._output_type = output_type

        self._stopped = False
        self._active = False

    def __call__(self, data):
        return self.perform_task(data)

    def run(self):
        raise NotImplementedError

    def perform_task(self, data):
        raise NotImplementedError

    def stop(self):
        self._stopped = True

    def stopped(self):
        return self._stopped

    @property
    def active(self):
        return self._active

    @property
    def input_type(self) -> type:
        if 'data' in self.perform_task.__annotations__:
            return self.perform_task.__annotations__['data']
        return self._input_type

    @property
    def output_type(self) -> type:
        if 'return' in self.perform_task.__annotations__:
            return self.perform_task.__annotations__['return']
        return self._output_type


class ComposedTask(Task):
    def __init__(self, tasks: List[Task], validate=False):
        super(Task, self).__init__()
        if len(tasks) < 2:
            raise TaskError('Not enough tasks for task composition. Please provide at least 2 tasks to compose')
        self.tasks = tasks

        if validate:
            self.validate_composition()

    def validate_composition(self):
        if not is_valid_composition(self.tasks):
            raise ValidationError('Invalid task composition - please provide tasks that can be composed correctly')

    def perform_task(self, data):
        return reduce(lambda x, task: task(x), self.tasks, data)

    def run(self):
        raise NotImplementedError

    @property
    def input_type(self):
        return self.tasks[0].input_type

    @property
    def output_type(self):
        return self.tasks[-1].output_type

    def stop(self):
        for task in self.tasks:
            task.stop()

    def stopped(self):
        return all(task.stopped() for task in self.tasks)


class IOTask(Task):
    def __init__(self, input_stream: InputStream, output_stream: OutputStream):
        super(IOTask, self).__init__(input_stream.stream_type, output_stream.stream_type)
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
            if type(data) is StreamState and data == StreamState.EOS:
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


class InputTask(Task):
    def __init__(self, input_stream: InputStream):
        super(InputTask, self).__init__(input_stream.stream_type)
        self._input_stream = input_stream

    @property
    def input_stream(self):
        return self._input_stream

    def run(self):
        for data in self.input_stream:
            if self.stopped():
                break
            self.perform_task(data)

    def stop(self):
        self.input_stream.close()
        super(InputTask, self).stop()

    def perform_task(self, data):
        raise NotImplementedError


class OutputTask(Task):
    def __init__(self, output_stream: OutputStream):
        super(OutputTask, self).__init__(output_type=output_stream.stream_type)
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


class TaskError(Exception):
    pass
