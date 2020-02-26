from unittest import TestCase, mock

import pytest

from frater.component import IOComponent, OutputComponent, InputComponent
from frater.component.builder import ComponentBuilder, ComponentBuildError


class SubIOComponent(IOComponent):
    pass


class SubOutputComponent(OutputComponent):
    pass


class SubInputComponent(InputComponent):
    pass


class TestComponent:
    pass


class TestComponentBuilder(TestCase):
    def setUp(self) -> None:
        with mock.patch('frater.stream.InputStream') as InputStream:
            self.input_stream = InputStream()

        with mock.patch('frater.stream.OutputStream') as OutputStream:
            self.output_stream = OutputStream()

        with mock.patch('frater.component.ComponentConfig') as ComponentConfig:
            self.config = ComponentConfig()

    def test_build_io_component(self):
        component = ComponentBuilder.build(SubIOComponent, self.config, self.input_stream, self.output_stream)
        assert isinstance(component, SubIOComponent)

        assert self.config == component.config
        assert self.input_stream == component.input_stream
        assert self.output_stream == component.output_stream

    def test_io_component_with_invalid_streams(self):
        # no streams
        with pytest.raises(ComponentBuildError):
            component = ComponentBuilder.build(SubIOComponent, self.config)

        # no output stream
        with pytest.raises(ComponentBuildError):
            component = ComponentBuilder.build(SubIOComponent, self.config, self.input_stream)

        # no input stream
        with pytest.raises(ComponentBuildError):
            component = ComponentBuilder.build(SubIOComponent, self.config, output_stream=self.output_stream)

    def test_build_output_component(self):
        component = ComponentBuilder.build(SubOutputComponent, self.config, output_stream=self.output_stream)
        assert isinstance(component, SubOutputComponent)

        assert self.config == component.config
        assert self.output_stream == component.output_stream

    def test_output_component_with_invalid_streams(self):
        # no output stream
        with pytest.raises(ComponentBuildError):
            component = ComponentBuilder.build(SubOutputComponent, self.config)

    def test_build_input_component(self):
        component = ComponentBuilder.build(SubInputComponent, self.config, input_stream=self.input_stream)
        assert isinstance(component, SubInputComponent)

        assert self.config == component.config
        assert self.input_stream == component.input_stream

    def test_input_component_with_invalid_streams(self):
        # no output stream
        with pytest.raises(ComponentBuildError):
            component = ComponentBuilder.build(SubInputComponent, self.config)

    def test_build_invalid_component(self):
        with pytest.raises(ComponentBuildError):
            component = ComponentBuilder.build(TestComponent, self.config, self.input_stream, self.output_stream)
