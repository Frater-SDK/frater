from typing import Dict

from frater.validation.json import validate_json
from .object import Object, ObjectType
from .object_defaults import JSON_DEFAULT
from ..proto import core
from ..trajectory.trajectory_factory import *

__all__ = ['json_to_object', 'object_to_json',
           'diva_format_to_object', 'object_to_diva_format',
           'protobuf_to_object', 'object_to_protobuf']


@validate_json(default=JSON_DEFAULT, completion=True)
def json_to_object(obj: Dict) -> Object:
    object_id = obj['_id']
    object_type = ObjectType(obj['object_type'])
    source_video = obj['source_video']
    experiment = obj['experiment']
    trajectory = json_to_trajectory(obj['trajectory'])

    return Object(object_type, source_video, experiment, trajectory, object_id)


def object_to_json(obj: Object) -> Dict:
    return {
        '_id': obj.object_id,
        'object_type': obj.object_type.value,
        'trajectory': trajectory_to_json(obj.trajectory),
        'source_video': obj.source_video,
        'experiment': obj.experiment
    }


def object_to_diva_format(obj: Object) -> Dict:
    return {
        'objectID': obj.object_id,
        'objectType': obj.object_type.long_name,
        'localization': {
            obj.source_video: {
                str(bounding_box.frame): {
                    'boundingBox': {
                        'x': bounding_box.x,
                        'y': bounding_box.y,
                        'w': bounding_box.w,
                        'h': bounding_box.h
                    },
                    'presenceConf': bounding_box.confidence
                } for bounding_box in obj.trajectory.bounding_boxes}}
    }


def diva_format_to_object(obj: Dict) -> Object:
    object_type = ObjectType.from_long_name(obj['objectType'])
    source_video = list(obj['localization'].keys())[0]
    trajectory = diva_format_to_trajectory(obj['localization'][source_video])
    object_id = obj['objectID']
    experiment = ''
    return Object(object_type, source_video, experiment, trajectory, object_id=object_id)


def protobuf_to_object(obj: core.Object) -> Object:
    object_id = obj.object_id
    object_type = ObjectType(obj.object_type)
    source_video = obj.source_video
    trajectory = protobuf_to_trajectory(obj.trajectory)
    experiment = obj.experiment
    return Object(object_type, source_video, experiment, trajectory, object_id)


def object_to_protobuf(obj: Object) -> core.Object:
    return core.Object(object_id=obj.object_id, object_type=obj.object_type.value,
                       source_video=obj.source_video, experiment=obj.experiment,
                       trajectory=trajectory_to_protobuf(obj.trajectory))
