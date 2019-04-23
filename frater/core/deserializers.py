from .activity import Activity
from .bounding_box import BoundingBox
from .factory.activity import json_to_activity
from .factory.bounding_box import json_to_bounding_box
from .factory.object import json_to_object
from .factory.temporal_range import json_to_temporal_range
from .factory.trajectory import json_to_trajectory
from .object import Object
from .trajectory import Trajectory

JSON_DESERIALIZERS = {
    Activity: json_to_activity,
    Object: json_to_object,
    Trajectory: json_to_trajectory,
    BoundingBox: json_to_bounding_box,
    'temporal_range': json_to_temporal_range
}


