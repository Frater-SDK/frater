import json
from typing import Callable

__all__ = ['json_deserializers', 'json_to_frater', 'get_kafka_deserializer']

from frater.data.data_type import data_types
from ..factory import Factory

json_deserializers = Factory()


def json_to_frater(data):
    d_type = data['data_type'] if 'data_type' in data else ''
    if isinstance(data, list):
        return [json_to_frater(item) for item in data]
    elif d_type in data_types:
        return data_types[d_type].from_dict(data)
    elif d_type in json_deserializers:
        return json_deserializers[d_type](data)
    else:
        return data


def get_kafka_deserializer() -> Callable:
    return lambda m: json_to_frater(json.loads(m.decode('utf-8')))
