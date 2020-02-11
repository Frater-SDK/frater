import time
from dataclasses import dataclass
from pprint import pformat
from typing import List

from frater.dependency.dependency import Dependency
from ...client.api import API
from ...component import ComponentClientConfig
from ...config import Config

__all__ = ['SystemClient', 'SystemClientConfig', 'get_system_client']


@dataclass
class SystemClientConfig(Config):
    host: str = ''
    port: str = ''
    polling_timeout: int = 3
    max_retries: int = 10


class SystemClient:
    def __init__(self, system_api: API, polling_timeout: int = 3, max_retries: int = 10):
        self.system_api = system_api
        self.polling_timeout = polling_timeout
        self.max_retries = max_retries

    def wait_for_dependencies(self, dependencies: List[Dependency]):
        all_ready = False
        retries = 0

        while not all_ready:
            dependency_statuses = [self.check_dependency(dependency) for dependency in dependencies]
            all_ready = all(status['ready'] for status in dependency_statuses)

            if not all_ready:
                retries += 1
                if retries >= self.max_retries:
                    raise TimeoutError(f'Took too long waiting for dependencies: {pformat(dependency_statuses)}')

                time.sleep(self.polling_timeout)

    def check_dependency(self, dependency: Dependency):
        return self.system_api.get('dependency', params=dependency.to_dict())

    def register_component(self, component_client_config: ComponentClientConfig):
        response = self.system_api.post('component/register', component_client_config.to_dict())
        return response.json()


def get_system_client(config: SystemClientConfig):
    api = API(config.host, config.port)
    return SystemClient(api, config.polling_timeout, config.max_retries)
