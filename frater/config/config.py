from dataclasses import dataclass, field
from typing import Dict
from uuid import uuid4


@dataclass
class Config:
    name: str = ''
    config_id: str = field(default_factory=lambda: str(uuid4()))
    meta: Dict = field(default_factory=dict)

    @classmethod
    def init_from_config_dict(cls, config: Dict):
        required_config, optional_config = cls.separate_config(config)
        return cls(**required_config, meta=optional_config)

    @classmethod
    def separate_config(cls, config: Dict):
        required_config = dict()
        optional_config = dict()

        annotations = get_config_annotations(cls)
        for name, val in config.items():
            if name in annotations:
                required_config[name] = val
            else:
                optional_config[name] = val

        return required_config, optional_config


def get_config_annotations(cls: type) -> Dict:
    annotations = dict()
    if issubclass(cls, Config) and cls is not Config:
        for super_class in cls.mro()[1:-1]:
            annotations.update(get_config_annotations(super_class))

    annotations.update(cls.__annotations__)

    return annotations


@dataclass
class TestConfig(Config):
    test_field: str = ''


def main():
    config_dict = {'hello': 'world', 'name': 'my_config_123456', 'test_field': 'this is a test'}

    config = Config.init_from_config_dict(config_dict)
    print(config)

    test_config = TestConfig.init_from_config_dict(config_dict)
    print(test_config)


if __name__ == '__main__':
    main()
