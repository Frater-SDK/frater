import json
from dataclasses import dataclass, field
from typing import Dict
from uuid import uuid4

import yaml
from dataclasses_json import DataClassJsonMixin


@dataclass
class Config(DataClassJsonMixin):
    name: str = 'config'
    config_id: str = field(default_factory=lambda: str(uuid4()))
    meta: Dict = field(default_factory=dict)

    def update_from_dict(self, d: Dict):
        for k, v in d.items():
            if k == 'meta':
                self.meta.update(v)
            if hasattr(self, k):
                k_class = type(getattr(self, k))
                if issubclass(k_class, Config):
                    v = k_class.from_dict(v)
                elif issubclass(k_class, DataClassJsonMixin):
                    v = k_class.from_dict(v)
                setattr(self, k, v)
            else:
                self.meta[k] = v

    def update_from_json(self, s: str):
        d = json.loads(s)
        self.update_from_dict(d)

    def update_from_yaml(self, s: str):
        d = yaml.load(s, yaml.FullLoader)
        self.update_from_dict(d)

    @classmethod
    def from_dict(cls, config: Dict, **kwargs):
        required_config, optional_config = cls.separate_config(config)
        return cls(**required_config, meta=optional_config)

    @classmethod
    def separate_config(cls, config: Dict):
        required_config = dict()
        optional_config = dict()

        annotations = get_config_annotations(cls)
        for key, value in config.items():
            if key == 'meta':
                optional_config.update(value)
            elif key in annotations:
                required_config[key] = process_config_value(annotations[key], value)
            else:
                optional_config[key] = value

        return required_config, optional_config

    @classmethod
    def from_yaml(cls, s: str, from_file=False):
        if from_file:
            with open(s) as f:
                return cls.from_dict(yaml.load(f, yaml.FullLoader))

        return cls.from_dict(yaml.load(s))

    def to_yaml(self, filename=''):
        d = self.to_dict()
        if filename:
            with open(filename, 'w') as f:
                return yaml.dump(d, f)

        return yaml.dump(d)


def process_config_value(annotation_type: type, value):
    if isinstance(value, list):
        list_type = getattr(annotation_type, '__args__')[0]
        return [process_config_value(list_type, item) for item in value]
    elif issubclass(annotation_type, Config):
        return annotation_type.from_dict(value)
    else:
        return value


def get_config_annotations(cls: type) -> Dict:
    annotations = dict()
    if issubclass(cls, Config) and cls is not Config:
        for super_class in cls.mro()[1:-1]:
            if super_class is DataClassJsonMixin:
                break
            annotations.update(get_config_annotations(super_class))

    annotations.update(cls.__annotations__)

    return annotations
