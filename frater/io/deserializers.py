import json
from typing import Callable

from ..core.activity.activity_factory import *
from ..core.bounding_box.bounding_box_factory import *
from ..core.frame.frame_factory import *
from ..core.object.object_factory import *
from ..core.temporal_range.temporal_range_factory import *
from ..core.trajectory.trajectory_factory import *
from ..core.video.video_factory import *
from ..utilities.stream import json_to_stream_state

__all__ = ['json_to_frater', 'get_kafka_deserializer']

JSON_DESERIALIZERS = {
    'activity': json_to_activity,
    'activity_proposal': json_to_activity_proposal,
    'object': json_to_object,
    'object_detection': json_to_object_detection,
    'trajectory': json_to_trajectory,
    'bounding_box': json_to_bounding_box,
    'temporal_range': json_to_temporal_range,
    'video': json_to_video,
    'frame': json_to_frame,
    'cropped_frame': json_to_cropped_frame,
    'stream_state': json_to_stream_state
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
