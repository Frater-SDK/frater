from dataclasses import dataclass, field
from typing import List
from uuid import uuid4

from ..object import Object
from ..trajectory import Trajectory


@dataclass
class ActivityProposal:
    proposal_id: str = field(default_factory=lambda: str(uuid4()))
    trajectory: Trajectory = field(default_factory=Trajectory)
    objects: List[Object] = field(default_factory=list)
    source_video: str = ''
    experiment: str = ''
    confidence: float = 0.0

    @property
    def temporal_range(self):
        return self.trajectory.temporal_range

    @property
    def start_frame(self):
        return self.temporal_range.start_frame

    @property
    def end_frame(self):
        return self.temporal_range.end_frame
