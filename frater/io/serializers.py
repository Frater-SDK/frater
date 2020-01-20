import json
from typing import Callable

from ..core import *
from ..core.activity.activity_factory import *
from ..core.bounding_box.bounding_box_factory import *
from ..core.frame.frame_factory import *
from ..core.object.object_factory import *
from ..core.temporal_range.temporal_range_factory import *
from ..core.trajectory.trajectory_factory import *
from ..core.video.video_factory import *
from ..utilities.json import is_json_serializable
from ..utilities.stream import StreamState, stream_state_to_json

__all__ = ['frater_to_json', 'get_kafka_serializer']

JSON_SERIALIZERS = {
    Activity: activity_to_json,
    ActivityProposal: activity_proposal_to_json,
    Object: object_to_json,
    ObjectDetection: object_detection_to_json,
    Trajectory: trajectory_to_json,
    BoundingBox: bounding_box_to_json,
    TemporalRange: temporal_range_to_json,
    Video: video_to_json,
    Frame: frame_to_json,
    CroppedFrame: cropped_frame_to_json,
    StreamState: stream_state_to_json
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
