from easydict import EasyDict

from frater.core import BoundingBox, Trajectory, ObjectType, Object, Activity, ActivityType
from frater.core.proto import core


class MockTypes:
    def __init__(self, name):
        self.name = name
        self._temporal_range = None
        self._bounding_box = None
        self._trajectory = None
        self._object = None
        self._activity = None

    @property
    def temporal_range(self):
        return self._temporal_range()

    @property
    def bounding_box(self):
        return self._bounding_box()

    @property
    def trajectory(self):
        return self._trajectory()

    @property
    def object(self):
        return self._object()

    @property
    def activity(self):
        return self._activity()


MOCKS = EasyDict({'proto': MockTypes('proto'), 'json': MockTypes('json'), 'frater': MockTypes('frater')})

# Temporal Range
MOCKS.proto._temporal_range = lambda: core.TemporalRange(start_frame=10, end_frame=15)
MOCKS.json._temporal_range = lambda: {'start_frame': 10, 'end_frame': 15}
MOCKS.frater._temporal_range = lambda: (10, 15)

# Bounding Box
MOCKS.proto._bounding_box = lambda: core.BoundingBox(x=10, y=10, w=15, h=15, confidence=0.23, frame=10)
MOCKS.json._bounding_box = lambda: {
    'x': 10,
    'y': 10,
    'w': 15,
    'h': 15,
    'confidence': 0.23,
    'frame': 10
}
MOCKS.frater._bounding_box = lambda: BoundingBox(x=10, y=10, w=15, h=15, confidence=0.23, frame=10)

# Trajectory
MOCKS.proto._trajectory = lambda: core.Trajectory(bounding_boxes=[MOCKS.proto.bounding_box] * 10,
                                                  temporal_range=MOCKS.proto.temporal_range, scale=1.4)
MOCKS.json._trajectory = lambda: {'bounding_boxes': [MOCKS.json.bounding_box] * 10,
                                  'temporal_range': MOCKS.json.temporal_range,
                                  'scale': 1.4}
MOCKS.frater._trajectory = lambda: Trajectory([MOCKS.frater.bounding_box] * 10, MOCKS.frater.temporal_range, 1.4)

# Object
MOCKS.proto._object = lambda: core.Object(object_id='sdf431', object_type=1,
                                          source_video='test.mp4', experiment='test',
                                          trajectory=MOCKS.proto.trajectory)
MOCKS.json._object = lambda: {
    '_id': 'sdf431',
    'object_type': 1,
    'source_video': 'test.mp4',
    'experiment': 'test',
    'trajectory': MOCKS.json.trajectory
}
MOCKS.frater._object = lambda: Object(object_id='sdf431', object_type=ObjectType.PERSON,
                                      source_video='test.mp4', experiment='test',
                                      trajectory=MOCKS.frater.trajectory)

# Activity
MOCKS.proto._activity = lambda: core.Activity(activity_id='1234', activity_type=5,
                                              temporal_range=MOCKS.proto.temporal_range,
                                              trajectory=MOCKS.proto.trajectory, objects=[MOCKS.proto.object] * 2,
                                              source_video='test.mp4', experiment='test', confidence=0.9)
MOCKS.json._activity = lambda: {
    '_id': '1234',
    'activity_type': 5,
    'temporal_range': MOCKS.json.temporal_range,
    'trajectory': MOCKS.json.trajectory,
    'objects': [MOCKS.json.object] * 2,
    'source_video': 'test.mp4',
    'experiment': 'test',
    'confidence': 0.9
}

MOCKS.frater._activity = lambda: Activity(activity_id='1234', activity_type=ActivityType.LOAD,
                                          temporal_range=MOCKS.frater.temporal_range,
                                          trajectory=MOCKS.frater.trajectory, objects=[MOCKS.frater.object] * 2,
                                          source_video='test.mp4', experiment='test', confidence=0.9)
