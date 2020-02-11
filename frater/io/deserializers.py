import json
from typing import Callable

__all__ = ['json_to_frater', 'get_kafka_deserializer', 'register_json_deserializer', 'unregister_json_deserializer']

JSON_DESERIALIZERS = {
}


def json_to_frater(data):
    d_type = data['data_type'] if 'data_type' in data else None

    if d_type in JSON_DESERIALIZERS:
        return JSON_DESERIALIZERS[d_type](data)
    else:
        return data


def get_kafka_deserializer() -> Callable:
    return lambda m: json_to_frater(json.loads(m.decode('utf-8')))


def register_json_deserializer(data_type: str, deserializer: Callable):
    if data_type in JSON_DESERIALIZERS:
        raise DeserializerExistsError(f'Deserializer {data_type} already exists. Please use a different data_type.')

    JSON_DESERIALIZERS[data_type] = deserializer


def unregister_json_deserializer(data_type: str):
    if data_type not in JSON_DESERIALIZERS:
        raise DeserializerDoesNotExistError(f'Deserializer {data_type} does not exist.')

    del JSON_DESERIALIZERS[data_type]


class DeserializerExistsError(Exception):
    pass


class DeserializerDoesNotExistError(Exception):
    pass
