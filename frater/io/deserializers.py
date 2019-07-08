import json
from typing import Callable

from frater.core.activity import *
from frater.core.bounding_box import *
from frater.core.frame import *
from frater.core.object import *
from frater.core.temporal_range import *
from frater.core.trajectory import *
from frater.stream.stream_state import json_to_stream_state
from frater.utilities.json import is_json_deserializable

JSON_DESERIALIZERS = {
    'activity': json_to_activity,
    'activity_proposal': json_to_activity_proposal,
    'object': json_to_object,
    'object_detection': json_to_object_detection,
    'trajectory': json_to_trajectory,
    'bounding_box': json_to_bounding_box,
    'temporal_range': json_to_temporal_range,
    'frame': json_to_frame,
    'cropped_frame': json_to_cropped_frame,
    'stream_state': json_to_stream_state

}

PROTO_DESERIALIZERS = {
    Activity: protobuf_to_activity,
    Object: protobuf_to_object,
    Trajectory: protobuf_to_trajectory,
    BoundingBox: protobuf_to_bounding_box,
    TemporalRange: protobuf_to_temporal_range
}


def json_to_frater(data):
    d_type = data['data_type'] if 'data_type' in data else None

    if d_type in JSON_DESERIALIZERS:
        return JSON_DESERIALIZERS[d_type](data)
    elif is_json_deserializable(data):
        return data
    else:
        raise TypeError(f'Object can\'t be deserialized from json: {data}')


def proto_to_frater(data, d_type):
    return PROTO_DESERIALIZERS[d_type](data)


def get_kafka_deserializer() -> Callable:
    return lambda m: json_to_frater(json.loads(m.decode('utf-8')))
