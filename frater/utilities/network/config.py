from dataclasses import dataclass

from frater.config import Config


@dataclass
class NetworkConfig(Config):
    name: str = 'network_config'
    host: str = '0.0.0.0'
    port: int = 3000
    protocol: str = 'http://'

    @property
    def uri(self) -> str:
        return f'{self.protocol}{self.host}:{self.port}'
