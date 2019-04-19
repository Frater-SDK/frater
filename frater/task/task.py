from functools import reduce

from .validation import is_valid_composition


class Task:
    def __call__(self, data):
        return self.perform_task(data)

    def run(self):
        raise NotImplementedError

    def perform_task(self, data):
        raise NotImplementedError


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






