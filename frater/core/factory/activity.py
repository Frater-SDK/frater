from typing import Dict

from .object import *
from .temporal_range import *
from .trajectory import *
from ..activity import Activity, ActivityType
from ..proto import core
from ...validation.json import validate_json

__all__ = ['json_to_activity', 'activity_to_json',
           'diva_format_to_activity', 'activity_to_diva_format',
           'protobuf_to_activity', 'activity_to_protobuf']


@validate_json(default=True, data_type=Activity)
def json_to_activity(activity: Dict) -> Activity:
    activity_id = activity['_id']
    activity_type = ActivityType(activity['activity_type'])
    objects = [json_to_object(obj) for obj in activity['objects']]
    temporal_range = json_to_temporal_range(activity['temporal_range'])
    source_video = activity['source_video']
    experiment = activity['experiment']
    confidence = activity['confidence']
    trajectory = json_to_trajectory(activity['trajectory'])
    return Activity(activity_type=activity_type, temporal_range=temporal_range, source_video=source_video,
                    experiment=experiment, objects=objects, trajectory=trajectory,
                    activity_id=activity_id, confidence=confidence)


def activity_to_json(activity: Activity) -> Dict:
    return {
        '_id': activity.activity_id,
        'activity_type': activity.activity_type.value,
        'objects': [object_to_json(obj) for obj in activity.objects],
        'trajectory': trajectory_to_json(activity.trajectory),
        'temporal_range': temporal_range_to_json(activity.temporal_range),
        'source_video': activity.source_video,
        'experiment': activity.experiment,
        'confidence': activity.confidence
    }


def diva_format_to_activity(activity: Dict) -> Activity:
    activity_type = ActivityType.from_long_name(activity['activity'])
    activity_id = activity['activityID']
    confidence = activity['presenceConf']
    source_video = list(activity['localization'].keys())[0]
    objects = [diva_format_to_object(obj) for obj in activity['objects']]
    ranges = list(int(r) for r in activity['localization'][source_video])
    temporal_range = min(ranges), max(ranges)
    experiment = ''

    return Activity(activity_type=activity_type, temporal_range=temporal_range, source_video=source_video,
                    experiment=experiment, objects=objects, activity_id=activity_id, confidence=confidence)


def activity_to_diva_format(activity: Activity) -> Dict:
    return {
        'activityID': activity.activity_id,
        'activity': activity.activity_type.long_name,
        'presenceConf': activity.confidence,
        'localization': {
            activity.source_video: {
                str(activity.temporal_range[0]): 1,
                str(activity.temporal_range[1]): 0
            }
        },
        'objects': [
            object_to_diva_format(obj) for obj in activity.objects
        ]
    }


def protobuf_to_activity(activity: core.Activity) -> Activity:
    activity_type = ActivityType(activity.activity_type)
    activity_id = activity.activity_id
    confidence = activity.confidence
    objects = [protobuf_to_object(obj) for obj in activity.objects]
    temporal_range = protobuf_to_temporal_range(activity.temporal_range)
    source_video = activity.source_video
    experiment = activity.experiment

    return Activity(activity_type, temporal_range, source_video, experiment, objects, activity_id, confidence)


def activity_to_protobuf(activity: Activity) -> core.Activity:
    return core.Activity(activity_id=activity.activity_id, activity_type=activity.activity_type.value,
                         objects=[object_to_protobuf(obj)
                                  for obj in activity.objects],
                         temporal_range=temporal_range_to_protobuf(activity.temporal_range),
                         source_video=activity.source_video, experiment=activity.experiment
                         )
