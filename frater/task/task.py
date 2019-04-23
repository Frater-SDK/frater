from functools import reduce

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
        elif self._input_type:
            return self._input_type
        else:
            raise ValueError('No input type defined')

    @property
    def output_type(self) -> type:
        if 'return' in self.perform_task.__annotations__:
            return self.perform_task.__annotations__['return']
        elif self._output_type:
            return self._output_type
        else:
            raise ValueError('No output type defined')


class ComposedTask(Task):
    def __init__(self, tasks):
        super(Task, self).__init__()
        self.tasks = tasks

    def validate(self):
        if not is_valid_composition(self.tasks):
            raise TypeError('Invalid task composition')

    def perform_task(self, data):
        return reduce(lambda x, task: task(x), self.tasks, data)

    def run(self):
        raise NotImplementedError
