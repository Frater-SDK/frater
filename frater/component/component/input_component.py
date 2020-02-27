from dataclasses import dataclass

from .component import Component, ComponentConfig
from ...stream import InputStream, is_end_of_stream, is_start_of_stream

__all__ = ['InputComponent', 'InputComponentConfig']


@dataclass
class InputComponentConfig(ComponentConfig):
    name: str = 'input_component_config'


class InputComponent(Component):
    def __init__(self, config: InputComponentConfig, input_stream: InputStream):
        super(InputComponent, self).__init__(config)
        self.input_stream = input_stream

    def run(self):
        self.start()
        for data in self.input_stream:
            if self.stopped:
                break
            if self.paused:
                self.wait()

            if is_start_of_stream(data):
                self.reset()
                self.set_active()
                self.on_start_of_stream(data)
            elif is_end_of_stream(data):
                self.on_end_of_stream(data)
                self.set_inactive()
            else:
                self.component_lifecycle(data)

        self.stop()

    def component_lifecycle(self, data):
        self.before_preprocess(data)
        preprocessed_input = self.preprocess(data)
        self.before_process(preprocessed_input)
        output = self.process(preprocessed_input)
        self.after_process(output)
        postprocessed_output = self.postprocess(output)
        self.after_postprocess(postprocessed_output)

    def before_preprocess(self, data):
        pass

    # noinspection PyMethodMayBeStatic
    def preprocess(self, data):
        return data

    def before_process(self, data):
        pass

    def process(self, data):
        raise NotImplementedError

    def after_process(self, data):
        pass

    # noinspection PyMethodMayBeStatic
    def postprocess(self, data):
        return data

    def after_postprocess(self, data):
        pass

    def on_end_of_stream(self, data):
        pass

    def on_start_of_stream(self, data):
        pass
