from dataclasses import dataclass, field
from uuid import uuid4

from .. import API
from ...component import ComponentConfig
from ...config import Config
from ...utilities import NetworkConfig

__all__ = ['ComponentClient', 'ComponentClientConfig', 'get_component_client_config']


@dataclass
class ComponentClientConfig(Config):
    name: str = 'component_client_config'
    component_id: str = field(default_factory=lambda: str(uuid4()))
    host: str = 'localhost'
    port: int = 3000


class ComponentClient:
    def __init__(self, config: ComponentClientConfig):
        self.config = config
        self.component_api = API(config.host, config.port)

    def start(self):
        return self.component_api.get('start')

    def started(self):
        return self.component_api.get('started')

    def stop(self):
        return self.component_api.get('stop')

    def stopped(self):
        return self.component_api.get('stopped')

    def toggle_pause(self):
        return self.component_api.get('toggle_pause')

    def pause(self):
        return self.component_api.get('pause')

    def unpause(self):
        return self.component_api.get('unpause')

    def paused(self):
        return self.component_api.get('paused')

    def active(self):
        return self.component_api.get('active')

    def reset(self):
        return self.component_api.get('reset')

    def error(self):
        return self.component_api.get('error')

    def update_config(self, config):
        return self.component_api.patch('config', config)

    def get_config(self):
        return self.component_api.get('config')

    def get_state(self):
        return self.component_api.get('state')

    def get_status(self):
        return self.component_api.get('status')

    def get_endpoints(self):
        return self.component_api.get('endpoints')


def get_component_client_config(component_config: ComponentConfig, network_config: NetworkConfig):
    return ComponentClientConfig(component_id=component_config.component_id, name=component_config.name,
                                 host=network_config.host, port=network_config.port)
