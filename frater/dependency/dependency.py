from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin


@dataclass
class Dependency(DataClassJsonMixin):
    name: str
    host: str
    port: int
