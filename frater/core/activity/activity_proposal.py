from dataclasses import dataclass
from typing import List

from ..object import Object
from ..temporal_range import TemporalRange
from ..trajectory import Trajectory


@dataclass
class ActivityProposal:
    def __init__(self, proposal_id='', temporal_range: TemporalRange = None, trajectory: Trajectory = None,
                 objects: List[Object] = None, source_video: str = '', experiment: str = '', confidence=0.0):
        if objects is None:
            objects = []
        if temporal_range is None:
            temporal_range = TemporalRange()
        if trajectory is None:
            trajectory = Trajectory(temporal_range=temporal_range)

        self.proposal_id = proposal_id
        self.temporal_range = temporal_range
        self.source_video = source_video
        self.experiment = experiment
        self.objects = objects
        self.trajectory = trajectory
        self.confidence = confidence

    def __eq__(self, other: 'ActivityProposal') -> bool:
        return (
                self.proposal_id == other.proposal_id and
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
        return 'Activity Proposal {act.proposal_id} - {act.activity_type.long_name}' \
               '\nObjects:\n{objects}' \
               '\nTemporal Range: {act.temporal_range}' \
               '\nSource Video: {act.source_video} ' \
               '\nExperiment: {act.experiment}' \
               '\nConfidence: {act.confidence}'.format(act=self, objects=objects_string)

    @property
    def start_frame(self):
        return self.temporal_range.start_frame

    @property
    def end_frame(self):
        return self.temporal_range.end_frame