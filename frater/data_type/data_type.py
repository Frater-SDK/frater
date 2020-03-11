from dataclasses import dataclass, field
from typing import Dict

import inflection
from dataclasses_json import DataClassJsonMixin
from dataclasses_json.core import Json

from frater.utilities import datetime


@dataclass
class DataType(DataClassJsonMixin):
    created: str = field(default_factory=datetime.now)
    updated: str = field(default_factory=datetime.now)
    accessed: str = field(default_factory=datetime.now)

    @classmethod
    def data_type(cls):
        return inflection.underscore(cls.__name__)

    def to_dict(self, encode_json=False) -> Dict[str, Json]:
        d = super(DataType, self).to_dict()
        d['data_type'] = self.data_type()

        return d
