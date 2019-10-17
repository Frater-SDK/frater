from ..object.object_summary import get_object_summary
from ..temporal_range.temporal_range_summary import get_temporal_range_summary
from ..trajectory.trajectory_summary import get_trajectory_summary

__all__ = ['get_activity_summary', 'get_activity_proposal_summary']


def get_activity_summary(activity, eol=' '):
    return (
        f'activity id: {activity.activity_id}{eol}'
        f'activity type: {activity.activity_type.long_name}{eol}'
        f'proposal id: {activity.proposal_id}{eol}'
        f'confidence: {activity.confidence:.3f}{eol}'
        f'temporal range: {get_temporal_range_summary(activity.temporal_range, eol)}'
        f'trajectory:{eol}{get_trajectory_summary(activity.trajectory, eol)}{eol}'
        f'objects:{eol}{eol.join([get_object_summary(object, eol) for object in activity.objects])}{eol}'
        f'probabilities: {[f"{p:.3f}" for p in activity.probabilities]}{eol}'
        f'source video: {activity.source_video}{eol}'
        f'experiment: {activity.experiment}{eol}'
    )


def get_activity_proposal_summary(activity_proposal, eol=' '):
    return (
        f'activity proposal id {activity_proposal.proposal_id}{eol}'
        f'temporal range: {get_temporal_range_summary(activity_proposal.temporal_range, eol)}'
        f'trajectory:{eol}{get_trajectory_summary(activity_proposal.trajectory, eol)}{eol}'
        f'objects:{eol}{eol.join([get_object_summary(object, eol) for object in activity_proposal.objects])}{eol}'
        f'source video: {activity_proposal.source_video}{eol}'
        f'experiment: {activity_proposal.experiment}{eol}'
    )
