from .temporal_range import TemporalRange

__all__ = ['compute_temporal_iou']


def compute_temporal_iou(t_0: TemporalRange, t_1: TemporalRange) -> float:
    intersection = min(t_0.end_frame, t_1.end_frame) - max(t_0.start_frame, t_1.start_frame)
    union = max(t_0.end_frame, t_1.end_frame) - min(t_0.start_frame, t_1.start_frame)

    if union == 0:
        return 0.0
    
    return max(0.0, intersection / union)
