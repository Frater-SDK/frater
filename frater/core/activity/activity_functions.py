from .activity import Activity
from .activity_proposal import ActivityProposal
from .activity_type import ActivityType

__all__ = ['activity_to_proposal']


def proposal_to_activity(proposal: ActivityProposal,
                         activity_type: ActivityType = ActivityType.NULL,
                         confidence: float = 0.0):
    return Activity(activity_id=proposal.proposal_id,
                    activity_type=activity_type,
                    trajectory=proposal.trajectory,
                    objects=proposal.objects,
                    source_video=proposal.source_video,
                    experiment=proposal.experiment,
                    confidence=confidence)


def activity_to_proposal(activity: Activity):
    return ActivityProposal(proposal_id=activity.activity_id,
                            trajectory=activity.trajectory,
                            objects=activity.objects,
                            source_video=activity.source_video,
                            experiment=activity.experiment)
