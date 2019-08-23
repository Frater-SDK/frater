from frater.task import Task


class MockValidationTask(Task):
    def __init__(self):
        super(MockValidationTask, self).__init__()

    def run(self):
        pass

    def perform_task(self, data):
        pass
