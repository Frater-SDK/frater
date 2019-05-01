import json
from typing import Callable

from ..core.activity import *
from ..core.bounding_box import *
from ..core.object import *
from ..core.temporal_range import *
from ..core.trajectory import *

JSON_SERIALIZERS = {
    Activity: activity_to_json,
    Object: object_to_json,
    Trajectory: trajectory_to_json,
    BoundingBox: bounding_box_to_json,
    TemporalRange: temporal_range_to_json
}

PROTO_SERIALIZERS = {
    Activity: activity_to_protobuf,
    Object: object_to_protobuf,
    Trajectory: trajectory_to_protobuf,
    BoundingBox: bounding_box_to_protobuf,
    TemporalRange: temporal_range_to_protobuf
}


def frater_to_json(data, d_type=None):
    if d_type is None:
        d_type = type(data)
    if d_type in JSON_SERIALIZERS:
        return JSON_SERIALIZERS[d_type](data)
    else:
        raise TypeError(f'Object can\'t be serialized to json: {data}')


def frater_to_proto(data, d_type=None):
    if d_type is None:
        d_type = type(data)
    if d_type in PROTO_SERIALIZERS:
        return PROTO_SERIALIZERS[d_type](data)
    else:
        raise TypeError(f'Object can\'t be serialized to protobuf: {data}')


def get_kafka_serializer(d_type=None) -> Callable:
    return lambda m: json.dumps(frater_to_json(m, d_type)).encode('utf-8')