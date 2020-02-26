import json
from typing import Callable

from ..data_type import DataType
from ..factory import Factory
from ..utilities.json import is_json_serializable

__all__ = ['json_serializers', 'frater_to_json', 'get_kafka_serializer']

json_serializers = Factory()


def frater_to_json(data):
    d_type = type(data)

    if isinstance(data, list):
        return [frater_to_json(item) for item in data]
    elif issubclass(d_type, DataType):
        return data.to_dict()
    elif d_type in json_serializers:
        return json_serializers[d_type](data)
    elif is_json_serializable(data):
        return data
    else:
        raise TypeError(f'Object can\'t be serialized to json: {data}')


def get_kafka_serializer() -> Callable:
    return lambda m: json.dumps(frater_to_json(m)).encode('utf-8')
