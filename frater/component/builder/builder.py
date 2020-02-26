from ..component import IOComponent, ComponentConfig, OutputComponent, InputComponent, Component

from ...stream import OutputStream, InputStream


class ComponentBuildError(BaseException):
    pass


class ComponentBuilder:
    @staticmethod
    def build(component_class: type, component_config: ComponentConfig,
              input_stream: InputStream = None, output_stream: OutputStream = None) -> Component:
        if issubclass(component_class, IOComponent):
            if input_stream is None or output_stream is None:
                raise ComponentBuildError(f'InputStream and OutputStream may not be None for IOComponent')
            return component_class(component_config, input_stream, output_stream)
        elif issubclass(component_class, OutputComponent):
            if output_stream is None:
                raise ComponentBuildError(f'OutputStream may not be None for OutputComponent')
            return component_class(component_config, output_stream)
        elif issubclass(component_class, InputComponent):
            if input_stream is None:
                raise ComponentBuildError(f'InputStream may not be None for InputComponent')
            return component_class(component_config, input_stream)
        else:
            raise ComponentBuildError(f'Type {component_class} is not a valid component')
