from dataclasses import dataclass, field
from typing import List

from .stream import InputStream, OutputStream, StreamConfig
from ..config import Config
from ..dependency import Dependency
from ..factory import ObjectFactory

__all__ = ['InputStreamFactoryConfig', 'OutputStreamFactoryConfig',
           'StreamFactoryConfig', 'input_stream_factory', 'input_stream_configs',
           'output_stream_factory', 'output_stream_configs']

input_stream_factory = ObjectFactory(InputStream)
input_stream_configs = ObjectFactory(StreamConfig)

output_stream_factory = ObjectFactory(OutputStream)
output_stream_configs = ObjectFactory(StreamConfig)


@dataclass
class InputStreamFactoryConfig(Config):
    name: str = 'input_stream_factory_config'
    stream_type: str = ''
    data_type: str = ''
    stream_config: dict = field(default_factory=dict)
    dependencies: List[Dependency] = field(default_factory=list)


@dataclass
class OutputStreamFactoryConfig(Config):
    name: str = 'output_stream_factory_config'
    stream_type: str = ''
    data_type: str = ''
    stream_config: dict = field(default_factory=dict)
    dependencies: List[Dependency] = field(default_factory=list)


@dataclass
class StreamFactoryConfig(Config):
    name: str = 'stream_factory_config'
    input_stream_config: InputStreamFactoryConfig = field(default_factory=InputStreamFactoryConfig)
    output_stream_configs: List[OutputStreamFactoryConfig] = field(default_factory=list)

    @property
    def dependencies(self):
        dependencies = list()
        dependencies.extend(self.input_stream_config.dependencies)
        for config in self.output_stream_configs:
            dependencies.extend(config.dependencies)

        return dependencies
