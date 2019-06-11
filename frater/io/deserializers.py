import json
from typing import Callable

from frater.core.activity import *
from frater.core.bounding_box import *
from frater.core.frame import *
from frater.core.object import *
from frater.core.temporal_range import *
from frater.core.trajectory import *

JSON_DESERIALIZERS = {
    Activity: json_to_activity,
    Object: json_to_object,
    ObjectDetection: json_to_object_detection,
    Trajectory: json_to_trajectory,
    BoundingBox: json_to_bounding_box,
    TemporalRange: json_to_temporal_range,
    Frame: json_to_frame,
    CroppedFrame: json_to_cropped_frame,
}

PROTO_DESERIALIZERS = {
    Activity: protobuf_to_activity,
    Object: protobuf_to_object,
    Trajectory: protobuf_to_trajectory,
    BoundingBox: protobuf_to_bounding_box,
    TemporalRange: protobuf_to_temporal_range
}


def json_to_frater(data, d_type):
    if d_type in JSON_DESERIALIZERS:
        return JSON_DESERIALIZERS[d_type](data)
    else:
        return data


def proto_to_frater(data, d_type):
    return PROTO_DESERIALIZERS[d_type](data)


def get_kafka_deserializer(stream_type: type) -> Callable:
    return lambda m: json_to_frater(json.loads(m.decode('utf-8')), stream_type)
