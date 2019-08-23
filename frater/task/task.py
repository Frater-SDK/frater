import logging

logger = logging.getLogger()


class Task:
    def __init__(self):
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

    @property
    def stopped(self):
        return self._stopped

    @property
    def active(self):
        return self._active


class TaskError(Exception):
    pass
