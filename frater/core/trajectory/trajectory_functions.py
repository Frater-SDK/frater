from .trajectory import Trajectory

__all__ = ['compute_spatiotemporal_iou']


def compute_spatiotemporal_iou(trajectory: Trajectory, other_trajectory: Trajectory) -> float:
    intersection = trajectory.intersect(other_trajectory).volume()
    union = trajectory.volume() + other_trajectory.volume() - intersection
    if union <= 0:
        return 0.0
    return intersection / union
