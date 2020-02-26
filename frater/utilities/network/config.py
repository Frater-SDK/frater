import socket
from dataclasses import dataclass

from frater.config import Config


@dataclass
class NetworkConfig(Config):
    name: str = 'network_config'
    host: str = socket.gethostname()
    port: int = 3000
