from typing import List

from .activity_type import ActivityType
from ..object import Object
from ..temporal_range import TemporalRange
from ..trajectory import Trajectory


class Activity:
    def __init__(self, activity_type: ActivityType = ActivityType.NULL,
                 temporal_range: TemporalRange = None, source_video: str = '', experiment: str = '',
                 objects: List[Object] = None, trajectory: Trajectory = None, activity_id='', confidence=0.0):
        if objects is None:
            objects = []
        if temporal_range is None:
            temporal_range = TemporalRange()
        if trajectory is None:
            trajectory = Trajectory(temporal_range=temporal_range)

        self._activity_id = activity_id
        self._activity_type = activity_type
        self._temporal_range = temporal_range
        self._source_video = source_video
        self._experiment = experiment
        self._objects = objects
        self._trajectory = trajectory
        self._confidence = confidence

    def __eq__(self, other: 'Activity') -> bool:
        return (
                self.activity_id == other.activity_id and
                self.activity_type == other.activity_type and
                self.temporal_range == other.temporal_range and
                self.source_video == other.source_video and
                self.experiment == other.experiment and
                self.objects == other.objects and
                self.trajectory == other.trajectory and
                self.confidence == other.confidence
        )

    def __repr__(self):
        return self.__str__().replace('\n', ' ')

    def __str__(self):
        objects_string = '\n'.join('{obj}'.format(obj=obj)
                                   for obj in self.objects)
        return 'Activity {act.activity_id} - {act.activity_type.long_name}' \
               '\nObjects:\n{objects}' \
               '\nTemporal Range: {act.temporal_range}' \
               '\nSource Video: {act.source_video} ' \
               '\nExperiment: {act.experiment}' \
               '\nConfidence: {act.confidence}'.format(act=self, objects=objects_string)

    @property
    def activity_id(self):
        return self._activity_id

    @property
    def activity_type(self) -> ActivityType:
        return self._activity_type

    @property
    def objects(self) -> List[Object]:
        return self._objects

    @property
    def trajectory(self) -> Trajectory:
        return self._trajectory

    @property
    def temporal_range(self) -> TemporalRange:
        return self._temporal_range

    @property
    def source_video(self) -> str:
        return self._source_video

    @property
    def experiment(self) -> str:
        return self._experiment

    @property
    def confidence(self):
        return self._confidence

    @property
    def start_frame(self):
        return self.temporal_range.start_frame

    @property
    def end_frame(self):
        return self.temporal_range.end_frame
