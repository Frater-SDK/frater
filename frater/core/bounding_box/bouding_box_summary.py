__all__ = ['get_bounding_box_summary']


def get_bounding_box_summary(bounding_box, eol=' '):
    return (
        f'x0: {bounding_box.x:.3f} y0: {bounding_box.y:.3f}{eol}'
        f'x1: {bounding_box.x_1:.3f} y1: {bounding_box.y_1:.3f}{eol}'
        f'width: {bounding_box.w:.3f} height: {bounding_box.h:.3f}{eol}'
        f'frame index: {bounding_box.frame_index} confidence: {bounding_box.confidence:.3f}{eol}'
    )
