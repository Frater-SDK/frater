from ..bounding_box import get_bounding_box_summary
from ..trajectory import get_trajectory_summary

__all__ = ['get_object_summary', 'get_object_detection_summary']


def get_object_summary(object, eol=' '):
    return (
        f'object id: {object.object_id}{eol}'
        f'object type: {object.object_type.long_name}{eol}'
        f'trajectory:{eol}{get_trajectory_summary(object.trajectory, eol)}{eol}'
        f'source video: {object.source_video}{eol}'
        f'experiment: {object.experiment}{eol}'
    )


def get_object_detection_summary(object_detection, eol=' '):
    return (
        f'object detection id: {object_detection.object_detection_id}{eol}'
        f'object type: {object_detection.object_type.long_name}{eol}'
        f'bounding box: {eol}{get_bounding_box_summary(object_detection.bounding_box, eol)}{eol}'
        f'source video: {object_detection.source_video}{eol}'
        f'source image: {object_detection.source_image}{eol}'
        f'experiment: {object_detection.experiment}{eol}'
    )
