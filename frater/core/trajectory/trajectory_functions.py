from .trajectory import Trajectory

__all__ = ['compute_spatiotemporal_iou']


def compute_spatiotemporal_iou(trajectory: Trajectory, other_trajectory: Trajectory) -> float:
    intersection = trajectory.intersect(other_trajectory).volume()
    union = trajectory.volume() + other_trajectory.volume() - intersection
    return intersection / union
