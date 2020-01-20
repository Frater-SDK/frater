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
    """Activity is a container class that represents an activity that appears in the associated video
    including its spatiotemporal location in the video, the objects corresponding to the activity, the
    activity type, and other metadata.

    The activity's spatiotemporal location is represented by a :py:class:`~frater.core.trajectory.Trajectory`

    **Examples**

    >>> boxes = [BoundingBox(10.0, 15.0, 20.0, 20.0, 1.0, 10), BoundingBox(10.0, 15.0, 20.0, 20.0, 1.0, 20)]
    >>> activity = Activity(trajectory=Trajectory(boxes), activity_type=ActivityType.HAND_INTERACTION)
    >>> activity.trajectory.bounding_boxes[0]
    [1] BoundingBox(x=10.0, y=15.0, w=20.0, h=20.0, confidence=1.0, frame_index=10)
    >>> len(activity)
    [2] 11

    """
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
        """
        :py:func:`__len__` gives the length of the activity, which is defined by the length of its :py:class:`~frater.core.temporal_range.TemporalRange`

        :return: returns length of activity
        :rtype: int
        """
        return len(self.temporal_range)

    def __getitem__(self, item: Union[int, slice]) -> Union[BoundingBox, 'Activity']:
        """

        :param item:
        :return:

        """
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
    def init_from_activity_proposal(cls, proposal: ActivityProposal, activity_type: ActivityType = ActivityType.NULL,
                                    confidence: float = 0.0, probabilities: List[float] = None):
        """This function is used to instantiate a new :py:class:`~frater.core.activity.Activity` based on the provided
        :py:class:`~frater.core.activity.ActivityProposal`

        :param ActivityProposal proposal: proposal for building new activity
        :param ActivityType activity_type: activity type of the new activity
        :param float confidence: confidence of the activity
        :param List[float] probabilities: list of probabilities for the possible activity types
        :return: returns an :py:class:`~frater.core.activity.Activity` built from provided :py:class:`~frater.core.activity.ActivityProposal`
        :rtype: Activity

        """
        if probabilities is None:
            probabilities = []

        return Activity(proposal_id=proposal.proposal_id, activity_type=activity_type,
                        trajectory=proposal.trajectory, objects=proposal.objects,
                        source_video=proposal.source_video, experiment=proposal.experiment,
                        confidence=confidence, probabilities=probabilities)
