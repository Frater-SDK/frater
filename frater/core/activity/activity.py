from dataclasses import dataclass, field
from typing import List, Union
from uuid import uuid4

from .activity_proposal import ActivityProposal
from .activity_summary import get_activity_summary
from .activity_type import ActivityType
from ..bounding_box import BoundingBox
from ..object import Object
from ..trajectory import Trajectory
from ...logging import get_summary


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

    def __len__(self):
        return len(self.temporal_range)

    def __getitem__(self, item: Union[int, slice]) -> Union[BoundingBox, 'Activity']:
        if isinstance(item, int):
            return self.trajectory[item]
        elif isinstance(item, slice):
            trajectory = self.trajectory[item]
            objects = [object[max(item.start, object.start_frame):min(item.stop, object.end_frame)]
                       for object in self.objects]

            return Activity(self.activity_id, self.proposal_id, self.activity_type,
                            trajectory, objects, self.source_video, self.experiment,
                            self.confidence, self.probabilities)

    @property
    def temporal_range(self):
        return self.trajectory.temporal_range

    @property
    def start_frame(self):
        return self.temporal_range.start_frame

    @property
    def end_frame(self):
        return self.temporal_range.end_frame

    def summary(self, multiline=True):
        return get_summary(self, get_activity_summary, multiline)

    @classmethod
    def init_from_activity_proposal(cls, proposal: ActivityProposal,
                                    activity_type: ActivityType = ActivityType.NULL,
                                    confidence: float = 0.0, probabilities: List[float] = None):
        return Activity(proposal_id=proposal.proposal_id, activity_type=activity_type,
                        trajectory=proposal.trajectory, objects=proposal.objects,
                        source_video=proposal.source_video, experiment=proposal.experiment,
                        confidence=confidence, probabilities=probabilities)
