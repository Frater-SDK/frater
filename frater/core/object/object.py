import copy
from typing import Union

from .object_type import ObjectType
from ..bounding_box import BoundingBox
from ..temporal_range import TemporalRange
from ..trajectory import Trajectory


class Object:
    def __init__(self, object_id: str = '', object_type: ObjectType = ObjectType.NULL,
                 trajectory: Trajectory = None, source_video: str = '', experiment: str = ''):
        self.object_id = object_id
        self.object_type = object_type

        if trajectory is None:
            self.trajectory = Trajectory()
        else:
            self.trajectory = trajectory

        self.source_video = source_video
        self.experiment = experiment

    def __eq__(self, other: 'Object') -> bool:
        return (
                self.object_id == other.object_id and
                self.object_type == other.object_type and
                self.source_video == other.source_video and
                self.trajectory == other.trajectory and
                self.experiment == other.experiment
        )

    def __str__(self):
        return '{obj.object_id} - {obj.object_type.long_name} - ' \
               '{obj.trajectory.temporal_range} - {obj.source_video}'.format(obj=self)

    def __getitem__(self, item) -> Union[BoundingBox, 'Object']:
        if isinstance(item, int):
            return self.trajectory[item]
        elif isinstance(item, slice):
            trajectory = self.trajectory[item]
            object = copy.deepcopy(self)
            object._trajectory = trajectory

            return object

    @property
    def temporal_range(self) -> TemporalRange:
        return self.trajectory.temporal_range

    @property
    def start_frame(self) -> int:
        return self.temporal_range.start_frame

    @property
    def end_frame(self) -> int:
        return self.temporal_range.end_frame
