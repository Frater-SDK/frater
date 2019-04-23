import json
from typing import Callable

from frater.core import JSON_DESERIALIZERS
from ..core import JSON_SERIALIZERS


def get_json_serializer(stream_type: type) -> Callable:
    if stream_type in JSON_SERIALIZERS:
        return JSON_SERIALIZERS[stream_type]
    else:
        raise TypeError('Type {} is not currently supported for streaming on Kafka'.format(stream_type))


def get_kafka_serializer(stream_type: type) -> Callable:
    return lambda m: json.dumps(get_json_serializer(stream_type)(m)).encode('utf-8')


def get_json_deserializer(stream_type: type) -> Callable:
    if stream_type in JSON_DESERIALIZERS:
        return JSON_DESERIALIZERS[stream_type]
    else:
        raise TypeError('Type {} is not currently supported for streaming on Kafka'.format(stream_type))


def get_kafka_deserializer(stream_type: type) -> Callable:
    return lambda m: get_json_deserializer(stream_type)(json.loads(m.decode('utf-8')))
