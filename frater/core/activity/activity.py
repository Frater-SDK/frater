from dataclasses import dataclass, field
from typing import List
from uuid import uuid4

from .activity_type import ActivityType
from ..object import Object
from ..trajectory import Trajectory


@dataclass
class Activity:
    activity_id: str = field(default_factory=lambda: str(uuid4()))
    proposal_id: str = ''
    activity_type: ActivityType = field(default=ActivityType.NULL)
    trajectory: Trajectory = field(default_factory=Trajectory)
    objects: List[Object] = field(default_factory=list)
    source_video: str = ''
    experiment: str = ''
    confidence: float = 0.0
    probabilities: List[float] = field(default_factory=lambda: [0.0] * len(ActivityType))

    @property
    def temporal_range(self):
        return self.trajectory.temporal_range

    @property
    def start_frame(self):
        return self.temporal_range.start_frame

    @property
    def end_frame(self):
        return self.temporal_range.end_frame
