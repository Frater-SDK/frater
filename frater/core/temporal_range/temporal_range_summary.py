__all__ = ['get_temporal_range_summary']


def get_temporal_range_summary(temporal_range, eol=' '):
    return (
        f'start: {temporal_range.start_frame}, end: {temporal_range.end_frame}{eol}'
    )
