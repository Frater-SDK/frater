from dataclasses import dataclass, field
from typing import Callable, List

from frater.component.builder import ComponentBuilder
from frater.component.client import get_component_client_config
from frater.component.component import ComponentConfig
from frater.component.manager import ComponentManager
from frater.config import Config
from frater.server import ServerManager, get_default_middleware, NetworkConfig
from frater.stream import StreamFactoryConfig
from frater.stream.factory import stream_factory
from frater.system import get_system_client, SystemClientConfig


@dataclass
class ComponentServerConfig(Config):
    component_config: ComponentConfig = field(default_factory=ComponentConfig)
    stream_config: StreamFactoryConfig = field(default_factory=StreamFactoryConfig)
    system_config: SystemClientConfig = field(default_factory=SystemClientConfig)
    network_config: NetworkConfig = field(default_factory=NetworkConfig)


def serve_component(component_class: type, serving_config: ComponentServerConfig, middleware: List[Callable] = None):
    # connect to system manager
    system_client = get_system_client(serving_config.system_config)
    # check dependencies for streams
    system_client.wait_for_dependencies(serving_config.stream_config.dependencies)
    # create streams
    input_stream, output_stream = stream_factory(serving_config.stream_config)
    # check dependencies for component
    system_client.wait_for_dependencies(serving_config.component_config.dependencies)
    # create component
    component = ComponentBuilder.build(component_class, serving_config.component_config, input_stream, output_stream)
    # create component manager
    component_manager = ComponentManager(component)
    # setup server
    if not middleware:
        middleware = get_default_middleware()
    server_manager = ServerManager(middleware)
    # register component endpoints with server
    component_manager.register_endpoints(server_manager)
    # register component with system
    client_config = get_component_client_config(serving_config.component_config, serving_config.network_config)
    system_client.register_component(client_config)

    return server_manager.get_server()
