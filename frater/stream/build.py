from typing import Tuple

from .factory import *
from .stream import InputStream, OutputStream, MultiOutputStream


def get_streams(config: StreamFactoryConfig) -> Tuple[InputStream, OutputStream]:
    input_stream = get_input_stream(config.input_stream_config)

    if len(config.output_stream_configs) == 0:
        output_stream = None
    elif len(config.output_stream_configs) > 1:
        output_streams = [get_output_stream(stream_config) for stream_config in config.output_stream_configs]
        output_stream = MultiOutputStream(output_streams)
    else:
        output_stream = get_output_stream(config.output_stream_configs[0])

    return input_stream, output_stream


def get_input_stream(config: InputStreamFactoryConfig) -> InputStream:
    if not config:
        return None
    else:
        stream_config = get_input_stream_config(config)
        return input_stream_factory[config.stream_type](stream_config)


def get_input_stream_config(config: InputStreamFactoryConfig):
    config_class = input_stream_configs[config.stream_type]
    return config_class.from_dict(config.stream_config)


def get_output_stream(config: OutputStreamFactoryConfig) -> OutputStream:
    if not config:
        return None
    else:
        stream_config = get_output_stream_config(config)
        return output_stream_factory[config.stream_type](stream_config)


def get_output_stream_config(config: OutputStreamFactoryConfig):
    config_class = output_stream_configs[config.stream_type]
    return config_class.from_dict(config.stream_config)
