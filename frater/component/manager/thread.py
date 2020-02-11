from threading import Thread
from typing import Optional

from ..component import Component


class ComponentThread(Thread):
    def __init__(self, component: Component):
        super(ComponentThread, self).__init__()
        self.component = component

        self.error = None
        self.started_once = False

    def run(self):
        try:
            self.component.run()
        except BaseException as e:
            self.error = e

        self.component.stop()

    def join(self, timeout: Optional[float] = ...) -> None:
        super(ComponentThread, self).join()
        if self.has_error():
            raise self.error

    def has_error(self):
        return self.error is not None

    def start(self):
        super(ComponentThread, self).start()
        self.started_once = True
