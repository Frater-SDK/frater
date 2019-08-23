from easydict import EasyDict

from frater.core import BoundingBox, Trajectory, ObjectType, Object, Activity, ActivityType, TemporalRange

__all__ = ['MOCKS']


class MockTypes:
    def __init__(self, name):
        self.name = name
        self._frame = None
        self._cropped_frame = None
        self._video = None
        self._temporal_range = None
        self._bounding_box = None
        self._trajectory = None
        self._object = None
        self._activity = None

    @property
    def frame(self):
        return self._frame()

    @property
    def cropped_frame(self):
        return self._cropped_frame()

    @property
    def video(self):
        return self.video()

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

    def get_mocks(self):
        return [self.temporal_range, self.bounding_box, self.trajectory, self.object, self.activity]


MOCKS = EasyDict({'json': MockTypes('json'), 'frater': MockTypes('frater')})

# Temporal Range
MOCKS.json._temporal_range = lambda: {'data_type': 'temporal_range', 'start_frame': 10, 'end_frame': 15}
MOCKS.frater._temporal_range = lambda: TemporalRange(10, 15)

# Bounding Box
MOCKS.json._bounding_box = lambda: {
    'data_type': 'bounding_box',
    'x': 10.0,
    'y': 10.0,
    'w': 15.0,
    'h': 15.0,
    'confidence': 0.23,
    'frame_index': 10
}
MOCKS.frater._bounding_box = lambda: BoundingBox(x=10.0, y=10.0, w=15.0, h=15.0, confidence=0.23, frame_index=10)

# Trajectory
json_boxes = [{
    'data_type': 'bounding_box',
    'x': 10.0,
    'y': 10.0,
    'w': 15.0,
    'h': 15.0,
    'confidence': 0.23,
    'frame_index': i + 1
} for i in range(10)]
frater_boxes = [BoundingBox(x=10.0, y=10.0, w=15.0, h=15.0, confidence=0.23, frame_index=i + 1) for i in range(10)]
MOCKS.json._trajectory = lambda: {'data_type': 'trajectory',
                                  'bounding_boxes': json_boxes}
MOCKS.frater._trajectory = lambda: Trajectory(frater_boxes)

# Object
MOCKS.json._object = lambda: {
    'data_type': 'object',
    'object_id': 'sdf431',
    'object_type': 1,
    'source_video': 'test.mp4',
    'experiment': 'test',
    'trajectory': MOCKS.json.trajectory
}
MOCKS.frater._object = lambda: Object(object_id='sdf431', object_type=ObjectType.DOOR,
                                      trajectory=MOCKS.frater.trajectory, source_video='test.mp4', experiment='test')

# Activity
MOCKS.json._activity = lambda: {
    'data_type': 'activity',
    'activity_id': '1234',
    'activity_proposal_id': '',
    'activity_type': 11,
    'trajectory': MOCKS.json.trajectory,
    'objects': [MOCKS.json.object] * 2,
    'source_video': 'test.mp4',
    'experiment': 'test',
    'confidence': 0.9,
    'probabilities': [0.0] * len(ActivityType)
}

MOCKS.frater._activity = lambda: Activity(activity_id='1234', activity_type=ActivityType.PERSON_LOADS_VEHICLE,
                                          trajectory=MOCKS.frater.trajectory, objects=[MOCKS.frater.object] * 2,
                                          source_video='test.mp4', experiment='test', confidence=0.9)
