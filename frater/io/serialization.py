import json
from typing import Callable

from ..core import Activity, Object
from ..core.factory.activity import activity_to_json, json_to_activity
from ..core.factory.object import object_to_json, json_to_object


def get_json_serializer(stream_type: type) -> Callable:
    if stream_type == Activity:
        return activity_to_json
    elif stream_type == Object:
        return object_to_json
    else:
        raise TypeError('Type {} is not currently supported for streaming on Kafka'.format(stream_type))


def get_kafka_serializer(stream_type: type) -> Callable:
    return lambda m: json.dumps(get_json_serializer(stream_type)(m)).encode('utf-8')


def get_json_deserializer(stream_type) -> Callable:
    if stream_type == Activity:
        return json_to_activity
    elif stream_type == Object:
        return json_to_object
    else:
        raise TypeError('Type {} is not currently supported for streaming on Kafka'.format(stream_type))


def get_kafka_deserializer(stream_type: type) -> Callable:
    return lambda m: get_json_deserializer(stream_type)(json.loads(m.decode('utf-8')))
