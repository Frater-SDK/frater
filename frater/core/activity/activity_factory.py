from typing import Dict

from .activity import Activity, ActivityType
from .activity_defaults import ACTIVITY_JSON_DEFAULT, ACTIVITY_PROPOSAL_JSON_DEFAULT
from .activity_proposal import ActivityProposal
from ..object.object_factory import *
from ..trajectory.trajectory_factory import *
from ...validation.json import validate_json

__all__ = ['json_to_activity', 'activity_to_json',
           'diva_format_to_activity', 'activity_to_diva_format',
           'json_to_activity_proposal', 'activity_proposal_to_json']


@validate_json(default=ACTIVITY_JSON_DEFAULT, completion=True)
def json_to_activity(activity: Dict) -> Activity:
    activity_id = activity['activity_id']
    proposal_id = activity['activity_proposal_id']
    activity_type = ActivityType(activity['activity_type'])
    objects = [json_to_object(obj) for obj in activity['objects']]
    source_video = activity['source_video']
    experiment = activity['experiment']
    confidence = activity['confidence']
    trajectory = json_to_trajectory(activity['trajectory'])
    probabilities = activity['probabilities']
    return Activity(activity_id=activity_id, proposal_id=proposal_id, activity_type=activity_type,
                    trajectory=trajectory, objects=objects, source_video=source_video,
                    experiment=experiment, confidence=confidence, probabilities=probabilities)


def activity_to_json(activity: Activity) -> Dict:
    return {
        'data_type': 'activity',
        'activity_id': activity.activity_id,
        'activity_proposal_id': activity.proposal_id,
        'activity_type': activity.activity_type.value,
        'objects': [object_to_json(obj) for obj in activity.objects],
        'trajectory': trajectory_to_json(activity.trajectory),
        'source_video': activity.source_video,
        'experiment': activity.experiment,
        'confidence': activity.confidence,
        'probabilities': activity.probabilities
    }


def diva_format_to_activity(activity: Dict) -> Activity:
    activity_type = ActivityType.from_long_name(activity['activity'])
    activity_id = activity['activityID']
    confidence = activity['presenceConf']
    source_video = list(activity['localization'].keys())[0]
    objects = [diva_format_to_object(obj) for obj in activity['objects']]
    trajectory = sum(object.trajectory for object in objects)
    experiment = ''

    return Activity(activity_id=activity_id, activity_type=activity_type, trajectory=trajectory, objects=objects,
                    source_video=source_video, experiment=experiment, confidence=confidence)


def activity_to_diva_format(activity: Activity) -> Dict:
    return {
        'activityID': activity.activity_id,
        'activity': activity.activity_type.long_name,
        'presenceConf': activity.confidence,
        'localization': {
            activity.source_video: {
                str(activity.temporal_range.start_frame): 1,
                str(activity.temporal_range.end_frame): 0
            }
        },
        'objects': [
            object_to_diva_format(obj) for obj in activity.objects
        ]
    }


@validate_json(default=ACTIVITY_PROPOSAL_JSON_DEFAULT, completion=True)
def json_to_activity_proposal(proposal: Dict) -> ActivityProposal:
    proposal_id = proposal['activity_proposal_id']
    objects = [json_to_object(obj) for obj in proposal['objects']]
    source_video = proposal['source_video']
    experiment = proposal['experiment']
    trajectory = json_to_trajectory(proposal['trajectory'])
    return ActivityProposal(proposal_id=proposal_id, trajectory=trajectory,
                            objects=objects, source_video=source_video,
                            experiment=experiment)


def activity_proposal_to_json(proposal: ActivityProposal) -> Dict:
    return {
        'data_type': 'activity_proposal',
        'activity_proposal_id': proposal.proposal_id,
        'objects': [object_to_json(obj) for obj in proposal.objects],
        'trajectory': trajectory_to_json(proposal.trajectory),
        'source_video': proposal.source_video,
        'experiment': proposal.experiment
    }
