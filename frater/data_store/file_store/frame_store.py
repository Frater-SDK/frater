import os
from functools import lru_cache

from PIL import Image

from frater.core import Frame, Modality, TemporalRange
from frater.data_store.file_store import FileStore


class FrameStore(FileStore):
    def __init__(self, root, extension='.jpeg', frame_filename_format='%08d%s', ignore_modality: bool = False):
        super(FrameStore, self).__init__(root)
        self.extension = extension
        self.frame_filename_format = frame_filename_format
        self.ignore_modality = ignore_modality

    @lru_cache(maxsize=128)
    def get_frame(self, video, frame_index, modality=Modality.RGB, experiment: str = '', timestamp: str = ''):
        frame_path = self.get_frame_path(video, modality, frame_index)
        frame_img = Image.open(frame_path)

        return Frame(frame_img, modality, index=frame_index, source_video=video,
                     experiment=experiment, timestamp=timestamp)

    def get_frames(self, video, frame_indices, modality=Modality.RGB, experiment: str = ''):
        return [self.get_frame(video, frame_index, modality, experiment) for frame_index in frame_indices]

    def get_frame_sequence(self, video, frame_range: TemporalRange, modality=Modality.RGB, experiment: str = ''):
        return self.get_frames(video, range(frame_range.start_frame, frame_range.end_frame + 1), modality, experiment)

    def get_frame_path(self, video, modality, frame_index):
        frame_filename = self.get_frame_filename(frame_index)
        if self.ignore_modality:
            return os.path.join(self.root, video, frame_filename)
        return os.path.join(self.root, video, modality.name, frame_filename)

    def get_frame_filename(self, frame_index):
        return self.frame_filename_format % (frame_index, self.extension)

    def load_image_for_frame(self, frame: Frame):
        return self.get_frame(frame.source_video, frame.index, frame.modality, frame.experiment, frame.experiment)
