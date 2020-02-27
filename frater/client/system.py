import time
from dataclasses import dataclass, field
from pprint import pformat
from typing import List, Dict

from .api import API
from .component import ComponentClientConfig
from ..config import Config
from ..dependency import Dependency
from ..utilities import NetworkConfig

__all__ = ['SystemClient', 'SystemClientConfig']


@dataclass
class SystemClientConfig(Config):
    name: str = 'system_client_config'
    network_config: NetworkConfig = field(default_factory=NetworkConfig)
    polling_timeout: int = 3
    max_retries: int = 10


class SystemClient:
    def __init__(self, config: SystemClientConfig):
        self.system_api = API(config.network_config.host, config.network_config.port)
        self.config = config

    def wait_for_dependencies(self, dependencies: List[Dependency]):
        if len(dependencies) == 0:
            return

        all_ready = False
        retries = 0

        while not all_ready:
            dependency_statuses = [self.check_dependency(dependency) for dependency in dependencies]
            all_ready = all(status['ready'] for status in dependency_statuses)

            if not all_ready:
                retries += 1
                if retries >= self.config.max_retries:
                    raise TimeoutError(f'Took too long waiting for dependencies: {pformat(dependency_statuses)}')

                time.sleep(self.config.polling_timeout)

    def check_dependency(self, dependency: Dependency):
        return self.system_api.get('/dependency', params=dependency.to_dict())

    def get_component(self, component_id: str):
        return self.system_api.get('/component', params={'component_id': component_id})

    def register_component(self, component_client_config: ComponentClientConfig):
        response = self.system_api.post('/component/register', component_client_config.to_dict())
        return response

    def start(self, component_id: str):
        return self.system_api.get('/component/start', params={'component_id': component_id})

    def started(self, component_id: str):
        return self.system_api.get('/component/started', params={'component_id': component_id})

    def stop(self, component_id: str):
        return self.system_api.get('/component/stop', params={'component_id': component_id})

    def stopped(self, component_id: str):
        return self.system_api.get('/component/stopped', params={'component_id': component_id})

    def toggle_pause(self, component_id: str):
        return self.system_api.get('/component/toggle_pause', params={'component_id': component_id})

    def pause(self, component_id: str):
        return self.system_api.get('/component/pause', params={'component_id': component_id})

    def unpause(self, component_id: str):
        return self.system_api.get('/component/unpause', params={'component_id': component_id})

    def paused(self, component_id: str):
        return self.system_api.get('/component/paused', params={'component_id': component_id})

    def active(self, component_id: str):
        return self.system_api.get('/component/active', params={'component_id': component_id})

    def reset(self, component_id: str):
        return self.system_api.get('/component/reset', params={'component_id': component_id})

    def error(self, component_id: str):
        return self.system_api.get('/component/error', params={'component_id': component_id})

    def get_config(self, component_id: str):
        return self.system_api.get('/component/config', params={'component_id': component_id})

    def update_config(self, component_id: str, config: Dict):
        return self.system_api.patch('/component/config', data={'component_id': component_id, 'config': config})

    def get_state(self, component_id: str):
        return self.system_api.get('/component/state', params={'component_id': component_id})

    def get_status(self, component_id: str):
        return self.system_api.get('/component/status', params={'component_id': component_id})

    def get_components(self):
        return self.system_api.get('/components')

    def start_all(self):
        return self.system_api.get('/components/start')

    def all_started(self):
        return self.system_api.get('/components/started')

    def stop_all(self):
        return self.system_api.get('/components/stop')

    def all_stopped(self):
        return self.system_api.get('/components/stopped')

    def toggle_pause_all(self):
        return self.system_api.get('/components/toggle_pause')

    def pause_all(self):
        return self.system_api.get('/components/pause')

    def unpause_all(self):
        return self.system_api.get('/components/unpause')

    def all_paused(self):
        return self.system_api.get('/components/paused')

    def all_active(self):
        return self.system_api.get('/components/active')

    def reset_all(self):
        return self.system_api.get('/components/reset')

    def all_error(self):
        return self.system_api.get('/components/error')

    def get_all_configs(self):
        return self.system_api.get('/components/config')

    def get_all_states(self):
        return self.system_api.get('/components/state')

    def get_all_statuses(self):
        return self.system_api.get('/components/status')
