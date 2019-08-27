__all__ = ['get_video_summary']


def get_video_summary(video, eol=' '):
    return (
        f'video name: {video.video_name}{eol}'
        f'experiment: {video.experiment}{eol}'
        f'width: {video.width}{eol}'
        f'height: {video.height}{eol}'
        f'framerate: {video.framerate}{eol}'
        f'start frame: {video.start_frame}{eol}'
        f'end frame: {video.end_frame}{eol}'
    )
