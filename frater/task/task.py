from functools import reduce
from typing import List

from ..stream import InputStream, OutputStream
from ..validation.error import ValidationError
from ..validation.task import is_valid_composition


class Task:
    def __init__(self, input_type=None, output_type=None):
        self._input_type = input_type
        self._output_type = output_type

    def __call__(self, data):
        return self.perform_task(data)

    def run(self):
        raise NotImplementedError

    def perform_task(self, data):
        raise NotImplementedError

    def stop(self):
        pass

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
            output = self.perform_task(data)
            self.output_stream(output)

    def perform_task(self, data):
        raise NotImplementedError


class InputTask(Task):
    def __init__(self, input_stream: InputStream):
        super(InputTask, self).__init__(input_stream.stream_type)
        self._input_stream = input_stream

    @property
    def input_stream(self):
        return self._input_stream

    def run(self):
        for data in self.input_stream:
            self.perform_task(data)

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
        while self.run_condition():
            output = self.perform_task()
            self.output_stream(output)

    def perform_task(self, **kwargs):
        raise NotImplementedError

    def run_condition(self) -> bool:
        raise NotImplementedError


class TaskError(Exception):
    pass
