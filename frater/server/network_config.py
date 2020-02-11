import socket
from dataclasses import dataclass

from ..config import Config


@dataclass
class NetworkConfig(Config):
    host: str = socket.gethostname()
    port: int = 3000
