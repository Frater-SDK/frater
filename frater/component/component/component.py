from dataclasses import dataclass, field
from typing import List
from uuid import uuid4

from dataclasses_json import DataClassJsonMixin

from ...config import Config
from ...dependency import Dependency
from ...stream import is_start_of_stream, is_end_of_stream
from ...utilities import Handler

__all__ = ['Component', 'ComponentConfig', 'ComponentState']


@dataclass
class ComponentConfig(Config):
    """Base
    :param component_id: Base :py:class:`~frater.config.Config` class for components
    """
    component_id: str = field(default_factory=lambda: str(uuid4()))
    name: str = 'component_config'
    dependencies: List[Dependency] = field(default_factory=list)


@dataclass
class ComponentState(DataClassJsonMixin):
    """
    :param state_id: test
    :type state_id: str
    """
    state_id: str = field(default_factory=lambda: str(uuid4()))


class Component:
    def __init__(self, config: ComponentConfig = None):
        """Base class for components in Frater. Generally shouldn't be used for direct subclassing, outside of\
        advanced use cases. In general, use :py:class:`~frater.component.component.io_component.IOComponent`,
        :py:class:`~frater.component.component.output_component.OutputComponent`, \
        :py:class:`~frater.component.component.input_component.InputComponent` or their subclasses as starting points.

        :param config: config object for the component. Should be a :py:class:`~frater.component.ComponentConfig` or a \
        subclass with more fields.
        """
        if config is None:
            config = ComponentConfig()

        self.started = False
        self.paused = False
        self.active = False

        self.config = config
        self.state = self.init_state()

    @property
    def stopped(self):
        return not self.started

    @property
    def _input_stream(self):
        return []

    def init_state(self) -> ComponentState:
        return ComponentState()

    def reset(self):
        self.state = self.init_state()

    def start(self):
        self.started = True

    def stop(self):
        self.set_inactive()
        self.started = False

    def pause(self):
        self.paused = True

    def unpause(self):
        self.paused = False

    def toggle_pause(self):
        self.paused = not self.paused

    def set_active(self):
        self.active = True

    def set_inactive(self):
        self.active = False

    def run(self):
        self.start()
        while self.started:
            for data in self._input_stream:
                if self.stopped:
                    break
                if self.paused:
                    self.wait()

                if is_start_of_stream(data):
                    self.reset()
                    self.set_active()
                    self.on_start_of_stream(data)
                    self.send_output(data)
                elif is_end_of_stream(data):
                    self.on_end_of_stream(data)
                    self.send_output(data)
                    self.set_inactive()
                else:
                    self.component_lifecycle(data)

    def wait(self):
        while self.paused:
            continue

    def component_lifecycle(self, data):
        self.before_preprocess(data)
        preprocessed_input = self.preprocess(data)
        self.before_process(preprocessed_input)
        output = self.process(preprocessed_input)
        self.after_process(output)
        postprocessed_output = self.postprocess(output)
        self.after_postprocess(postprocessed_output)
        self.send_output(postprocessed_output)

    def before_preprocess(self, data):
        pass

    def preprocess(self, data):
        return data

    def before_process(self, data):
        pass

    def process(self, data):
        raise NotImplementedError

    def after_process(self, data):
        pass

    def postprocess(self, data):
        return data

    def after_postprocess(self, data):
        pass

    def send_output(self, data):
        pass

    def on_start_of_stream(self, data):
        pass

    def on_end_of_stream(self, data):
        pass

    # noinspection PyMethodMayBeStatic
    def get_additional_handlers(self) -> List[Handler]:
        return []
