from functools import reduce
from typing import List

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


class TaskError(Exception):
    pass


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
