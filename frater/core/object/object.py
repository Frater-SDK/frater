from .object_type import ObjectType
from ..trajectory import Trajectory


class Object:
    def __init__(self, object_type: ObjectType = ObjectType.NULL,
                 source_video: str = '', experiment: str = '',
                 trajectory: Trajectory = None, object_id=''):
        self._object_id = object_id
        self._object_type = object_type
        self._source_video = source_video
        self._trajectory = trajectory
        self._experiment = experiment

    def __eq__(self, other: 'Object') -> bool:
        return (
                self.object_id == other.object_id and
                self.object_type == other.object_type and
                self.source_video == other.source_video and
                self.trajectory == other.trajectory and
                self.experiment == other.experiment
        )

    def __str__(self):
        return '{obj.object_id} - {obj.object_type.long_name} - {obj.trajectory.temporal_range}'.format(obj=self)
    
    @property
    def object_id(self):
        return self._object_id

    @property
    def object_type(self) -> ObjectType:
        return self._object_type

    @property
    def trajectory(self) -> Trajectory:
        return self._trajectory

    @property
    def source_video(self) -> str:
        return self._source_video

    @property
    def experiment(self) -> str:
        return self._experiment
