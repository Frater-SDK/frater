from typing import List

from .activity import Activity
from .activity_proposal import ActivityProposal
from .activity_type import ActivityType

__all__ = ['activity_to_proposal', 'proposal_to_activity']


def proposal_to_activity(proposal: ActivityProposal, activity_type: ActivityType = ActivityType.NULL,
                         confidence: float = 0.0, probabilities=None):
    """This function converts a proposal into an activity.

    :param ActivityProposal proposal: proposal for building new activity
    :param ActivityType activity_type: activity type of the new activity
    :param float confidence: confidence of the activity
    :param List[float] probabilities: list of probabilities for the possible activity types
    :return: returns an :py:class:`~frater.core.activity.Activity` built from provided :py:class:`~frater.core.activity.ActivityProposal`
    :rtype: Activity

    """
    if probabilities is None:
        probabilities = []

    return Activity(proposal_id=proposal.proposal_id, activity_type=activity_type, trajectory=proposal.trajectory,
                    objects=proposal.objects, source_video=proposal.source_video,
                    experiment=proposal.experiment, confidence=confidence, probabilities=probabilities)


def activity_to_proposal(activity: Activity) -> ActivityProposal:
    """This function converts an activity into a proposal


    :param Activity activity: activity to convert to proposal
    :return: the new activity proposal

    """
    return ActivityProposal(trajectory=activity.trajectory, objects=activity.objects,
                            source_video=activity.source_video, experiment=activity.experiment)
