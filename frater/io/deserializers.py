import json
from typing import Callable

from frater.core.activity import *
from frater.core.bounding_box import *
from frater.core.object import *
from frater.core.temporal_range import *
from frater.core.trajectory import *

JSON_DESERIALIZERS = {
    Activity: json_to_activity,
    Object: json_to_object,
    Trajectory: json_to_trajectory,
    BoundingBox: json_to_bounding_box,
    TemporalRange: json_to_temporal_range
}

PROTO_DESERIALIZERS = {
    Activity: protobuf_to_activity,
    Object: protobuf_to_object,
    Trajectory: protobuf_to_trajectory,
    BoundingBox: protobuf_to_bounding_box,
    TemporalRange: protobuf_to_temporal_range
}


def json_to_frater(data, d_type):
    return JSON_DESERIALIZERS[d_type](data)


def proto_to_frater(data, d_type):
    return JSON_DESERIALIZERS[d_type](data)


def get_kafka_deserializer(stream_type: type) -> Callable:
    return lambda m: json_to_frater(stream_type, json.loads(m.decode('utf-8')))
