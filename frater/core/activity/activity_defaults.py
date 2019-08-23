from .activity_type import ActivityType
from ..trajectory import trajectory_defaults

ACTIVITY_JSON_DEFAULT = {
    'activity_id': '',
    'activity_proposal_id': '',
    'activity_type': 0,
    'objects': [],
    'trajectory': trajectory_defaults.TRAJECTORY_JSON_DEFAULT,
    'source_video': '',
    'experiment': '',
    'confidence': 0.0,
    'probabilities': [0.0] * len(ActivityType)
}

ACTIVITY_PROPOSAL_JSON_DEFAULT = {
    'activity_proposal_id': '',
    'objects': [],
    'trajectory': trajectory_defaults.TRAJECTORY_JSON_DEFAULT,
    'source_video': '',
    'experiment': '',
}
