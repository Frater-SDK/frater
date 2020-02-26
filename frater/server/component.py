from dataclasses import dataclass, field
from typing import Callable, List

from .middleware import get_default_middleware
from .server_manager import ServerManager
from ..client import SystemClient, SystemClientConfig, get_component_client_config
from ..component import ComponentConfig, ComponentManager, ComponentBuilder
from ..config import Config
from ..stream import StreamFactoryConfig, get_streams
from ..utilities import NetworkConfig

__all__ = ['ComponentServerConfig', 'serve_component']


@dataclass
class ComponentServerConfig(Config):
    name: str = 'component_server_config'
    component_config: ComponentConfig = field(default_factory=ComponentConfig)
    stream_config: StreamFactoryConfig = field(default_factory=StreamFactoryConfig)
    system_config: SystemClientConfig = field(default_factory=SystemClientConfig)
    network_config: NetworkConfig = field(default_factory=NetworkConfig)


def serve_component(component_class: type, server_config: ComponentServerConfig, middleware: List[Callable] = None):
    # connect to system manager
    system_client = SystemClient(server_config.system_config)
    # check dependencies for streams
    system_client.wait_for_dependencies(server_config.stream_config.dependencies)
    # create streams
    input_stream, output_stream = get_streams(server_config.stream_config)
    # check dependencies for component
    system_client.wait_for_dependencies(server_config.component_config.dependencies)
    # create component
    component = ComponentBuilder.build(component_class, server_config.component_config, input_stream, output_stream)
    # create component manager
    component_manager = ComponentManager(component)
    # setup server
    if not middleware:
        middleware = get_default_middleware()
    server_manager = ServerManager(middleware)
    # register component endpoints with server
    server_manager.register_endpoints(component_manager.get_all_handlers())
    # register component with system
    client_config = get_component_client_config(server_config.component_config, server_config.network_config)
    system_client.register_component(client_config)
    return server_manager.get_server()
