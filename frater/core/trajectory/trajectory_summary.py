from ..bounding_box import get_bounding_box_summary

__all__ = ['get_trajectory_summary']


def get_trajectory_summary(trajectory, eol=' '):
    if len(trajectory) < 1:
        return None
    return (
        f'start: {eol}{get_bounding_box_summary(trajectory.bounding_boxes[0], eol)}{eol}'
        f'middle: {eol}{get_bounding_box_summary(trajectory.bounding_boxes[len(trajectory) // 2], eol)}{eol}'
        f'end: {eol}{get_bounding_box_summary(trajectory.bounding_boxes[-1], eol)}{eol}'
    )
