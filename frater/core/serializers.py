from .activity import Activity
from .bounding_box import BoundingBox
from .factory.activity import activity_to_json
from .factory.bounding_box import bounding_box_to_json
from .factory.object import object_to_json
from .factory.temporal_range import temporal_range_to_json
from .factory.trajectory import trajectory_to_json
from .object import Object
from .trajectory import Trajectory

JSON_SERIALIZERS = {
    Activity: activity_to_json,
    Object: object_to_json,
    Trajectory: trajectory_to_json,
    BoundingBox: bounding_box_to_json,
    'temporal_range': temporal_range_to_json
}
