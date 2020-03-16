from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin


@dataclass
class Dependency(DataClassJsonMixin):
    name: str = 'dependency'
    host: str = '0.0.0.0'
    port: int = 8080
