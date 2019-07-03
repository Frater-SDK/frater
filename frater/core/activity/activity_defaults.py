from ..temporal_range import temporal_range_defaults
from ..trajectory import trajectory_defaults

ACTIVITY_JSON_DEFAULT = {
    '_id': '',
    'proposal_id': '',
    'activity_type': 0,
    'objects': [],
    'trajectory': trajectory_defaults.TRAJECTORY_JSON_DEFAULT,
    'temporal_range': temporal_range_defaults.TEMPORAL_RANGE_JSON_DEFAULT,
    'source_video': '',
    'experiment': '',
    'confidence': 0.0
}

ACTIVITY_PROPOSAL_JSON_DEFAULT = {
    '_id': '',
    'objects': [],
    'trajectory': trajectory_defaults.TRAJECTORY_JSON_DEFAULT,
    'temporal_range': temporal_range_defaults.TEMPORAL_RANGE_JSON_DEFAULT,
    'source_video': '',
    'experiment': '',
    'confidence': 0.0
}
