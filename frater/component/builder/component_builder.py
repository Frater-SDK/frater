from ..component import IOComponent, ComponentConfig, OutputComponent, InputComponent, Component

from ...stream import OutputStream, InputStream


class ComponentBuildError(BaseException):
    pass


class ComponentBuilder:
    @classmethod
    def build(cls, component_class: type, component_config: ComponentConfig,
              input_stream: InputStream = None, output_stream: OutputStream = None) -> Component:
        if issubclass(component_class, IOComponent):
            return component_class(component_config, input_stream, output_stream)
        elif issubclass(component_class, OutputComponent):
            return component_class(component_config, output_stream)
        elif issubclass(component_class, InputComponent):
            return component_class(component_config, input_stream)
        else:
            raise ComponentBuildError(f'Type {component_class} is not a valid component class')
