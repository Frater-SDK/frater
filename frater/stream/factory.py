from dataclasses import dataclass, field
from typing import List, Tuple

from frater.dependency.dependency import Dependency
from .stream import InputStream, OutputStream, MultiOutputStream, StreamConfig
from ..config import Config

input_stream_factory_map = dict()
input_stream_config_factory_map = dict()

output_stream_factory_map = dict()
output_stream_config_factory_map = dict()


class InputStreamFactoryConfig(Config):
    name: str = 'input_stream_factory_config'
    stream_type: str = ''
    data_type: str = ''
    stream_config: dict = field(default_factory=dict)
    dependencies: List[Dependency] = field(default_factory=list)


class OutputStreamFactoryConfig(Config):
    name: str = 'output_stream_factory_config'
    stream_type: str = ''
    data_type: str = ''
    stream_config: dict = field(default_factory=dict)
    dependencies: List[Dependency] = field(default_factory=list)


@dataclass
class StreamFactoryConfig(Config):
    name: str = 'stream_factory_config'
    input_stream_config: InputStreamFactoryConfig = None
    output_stream_configs: List[OutputStreamFactoryConfig] = field(default_factory=list)

    @property
    def dependencies(self):
        dependencies = list()
        dependencies.extend(self.input_stream_config.dependencies)
        for config in self.output_stream_configs:
            dependencies.extend(config.dependencies)

        return dependencies


def stream_factory(config: StreamFactoryConfig) -> Tuple[InputStream, OutputStream]:
    input_stream = input_stream_factory(config.input_stream_config)

    if len(config.output_stream_configs) == 0:
        output_stream = None
    elif len(config.output_stream_configs) > 1:
        output_streams = [output_stream_factory(stream_config) for stream_config in config.output_stream_configs]
        output_stream = MultiOutputStream(output_streams)
    else:
        output_stream = output_stream_factory(config.output_stream_configs[0])

    return input_stream, output_stream


def input_stream_factory(config: InputStreamFactoryConfig) -> InputStream:
    if not config:
        return None
    else:
        stream_config = input_stream_config_factory(config)
        return input_stream_factory_map[config.stream_type](stream_config)


def input_stream_config_factory(config: InputStreamFactoryConfig):
    config_class = input_stream_config_factory_map[config.stream_type]
    return config_class.from_dict(config.stream_config)


def output_stream_factory(config: OutputStreamFactoryConfig) -> OutputStream:
    if not config:
        return None
    else:
        stream_config = output_stream_config_factory(config)
        return output_stream_factory_map[config.stream_type](stream_config)


def output_stream_config_factory(config: OutputStreamFactoryConfig):
    config_class = output_stream_config_factory_map[config.stream_type]
    return config_class.from_dict(config.stream_config)


def register_input_stream(input_stream: type, stream_type: str):
    if not issubclass(input_stream, InputStream):
        raise TypeError(f'{input_stream} is not a subclass of InputStream')
    elif stream_type in input_stream_factory_map:
        raise KeyError(f'stream type {stream_type} already exists')

    input_stream_factory_map[stream_type] = input_stream


def unregister_input_stream(stream_type: str):
    if stream_type not in input_stream_factory_map:
        raise KeyError(f'stream type {stream_type} does not exist')

    del input_stream_factory_map[stream_type]


def register_output_stream(output_stream: type, stream_type: str):
    if not issubclass(output_stream, OutputStream):
        raise TypeError(f'{output_stream} is not a subclass of OutputStream')
    elif stream_type in output_stream_factory_map:
        raise KeyError(f'stream type {stream_type} already exists')

    output_stream_factory_map[stream_type] = output_stream


def unregister_output_stream(stream_type: str):
    if stream_type not in output_stream_factory_map:
        raise KeyError(f'stream type {stream_type} does not exist')

    del output_stream_factory_map[stream_type]


def register_input_stream_config(input_stream_config: type, stream_type: str):
    if not issubclass(input_stream_config, StreamConfig):
        raise TypeError(f'{input_stream_config} is not a subclass of InputStream')
    elif stream_type in input_stream_config_factory_map:
        raise KeyError(f'stream type {stream_type} already exists')

    input_stream_factory_map[stream_type] = input_stream_config


def unregister_input_stream_config(stream_type: str):
    if stream_type not in input_stream_config_factory_map:
        raise KeyError(f'stream type {stream_type} does not exist')

    del input_stream_config_factory_map[stream_type]


def register_output_stream_config(output_stream_config: type, stream_type: str):
    if not issubclass(output_stream_config, StreamConfig):
        raise TypeError(f'{output_stream_config} is not a subclass of OutputStream')
    elif stream_type in output_stream_config_factory_map:
        raise KeyError(f'stream type {stream_type} already exists')

    output_stream_config_factory_map[stream_type] = output_stream_config


def unregister_output_stream_config(stream_type: str):
    if stream_type not in output_stream_config_factory_map:
        raise KeyError(f'stream type {stream_type} does not exist')

    del output_stream_config_factory_map[stream_type]
