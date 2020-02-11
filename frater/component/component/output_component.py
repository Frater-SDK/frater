from .component import Component, ComponentConfig
from ...stream import OutputStream

__all__ = ['OutputComponent']


class OutputComponent(Component):
    def __init__(self, config: ComponentConfig, output_stream: OutputStream):
        super(OutputComponent, self).__init__(config)
        self.output_stream = output_stream

    def run(self):
        self.start()
        while self.should_output() and not self.stopped:
            self.component_lifecycle()
        self.stop()

    def component_lifecycle(self):
        self.before_process()
        output = self.process()
        self.after_process(output)
        postprocessed_output = self.postprocess(output)
        self.after_postprocess(postprocessed_output)
        self.send_output(postprocessed_output)

    def before_process(self):
        pass

    def process(self):
        raise NotImplementedError

    def after_process(self, data):
        pass

    # noinspection PyMethodMayBeStatic
    def postprocess(self, data):
        return data

    def after_postprocess(self, data):
        pass

    # noinspection PyMethodMayBeStatic
    def should_output(self):
        return True

    def send_output(self, output):
        self.output_stream(output)
