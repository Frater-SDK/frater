from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin


@dataclass
class Category(DataClassJsonMixin):
    index: int = 0
    label: str = ''
    dataset: str = ''
