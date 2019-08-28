__all__ = ['get_frame_summary', 'get_cropped_frame_summary']


def get_frame_summary(frame, eol=' '):
    return (
        f'frame index: {frame.index}{eol}'
        f'source video: {frame.source_video}{eol}'
        f'modality: {frame.modality}{eol}'
        f'width: {frame.width}{eol}'
        f'height: {frame.height}{eol}'
        f'experiment: {frame.experiment}{eol}'
        f'timestamp: {frame.timestamp}{eol}'
    )


def get_cropped_frame_summary(cropped_frame, eol=' '):
    return get_frame_summary(cropped_frame, eol) + (
        f'source location: {cropped_frame.source_location}{eol}'
    )
