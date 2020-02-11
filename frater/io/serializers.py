import json
from typing import Callable

from ..utilities.json import is_json_serializable

__all__ = ['frater_to_json', 'get_kafka_serializer', 'register_json_serializer', 'unregister_json_serializer']

JSON_SERIALIZERS = {

}


def frater_to_json(data):
    d_type = type(data)

    if d_type in JSON_SERIALIZERS:
        return JSON_SERIALIZERS[d_type](data)
    elif is_json_serializable(data):
        return data
    else:
        raise TypeError(f'Object can\'t be serialized to json: {data}')


def get_kafka_serializer() -> Callable:
    return lambda m: json.dumps(frater_to_json(m)).encode('utf-8')


def register_json_serializer(data_type: type, serializer: Callable):
    if data_type in JSON_SERIALIZERS:
        raise SerializerExistsError(f'Serializer {data_type} already exists. Please use a different data_type.')

    JSON_SERIALIZERS[data_type] = serializer


def unregister_json_serializer(data_type: type):
    if data_type not in JSON_SERIALIZERS:
        raise SerializerDoesNotExistError(f'Serializer {data_type} does not exist.')

    del JSON_SERIALIZERS[data_type]


class SerializerExistsError(Exception):
    pass


class SerializerDoesNotExistError(Exception):
    pass
