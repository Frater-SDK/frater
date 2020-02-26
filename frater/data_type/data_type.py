from dataclasses import dataclass
from typing import Dict

import inflection
from dataclasses_json import DataClassJsonMixin
from dataclasses_json.core import Json


@dataclass
class DataType(DataClassJsonMixin):
    @classmethod
    def data_type(cls):
        return inflection.underscore(cls.__name__)

    def to_dict(self, encode_json=False) -> Dict[str, Json]:
        d = super(DataType, self).to_dict()
        d['data_type'] = self.data_type()

        return d
