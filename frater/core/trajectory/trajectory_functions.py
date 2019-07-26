from .trajectory import Trajectory
from ..bounding_box.bounding_box_functions import scale_bounding_box

__all__ = ['compute_spatiotemporal_iou', 'scale_trajectory']


def compute_spatiotemporal_iou(trajectory: Trajectory, other_trajectory: Trajectory, scale: float = 1.0) -> float:
    trajectory = scale_trajectory(trajectory, scale)
    other_trajectory = scale_trajectory(other_trajectory, scale)
    intersection = trajectory.intersect(other_trajectory).volume()
    union = trajectory.volume() + other_trajectory.volume() - intersection
    if union <= 0:
        return 0.0
    return intersection / union


def scale_trajectory(trajectory: Trajectory, scale: float = 1.0) -> Trajectory:
    bounding_boxes = [scale_bounding_box(bounding_box, scale) for bounding_box in trajectory.bounding_boxes]
    return Trajectory(bounding_boxes)
