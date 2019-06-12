import os
from functools import lru_cache

from PIL import Image

from .file_store import FileStore
from ...core import Frame, Modality, TemporalRange


class FrameStore(FileStore):
    def __init__(self, root, extension='.jpeg', frame_filename_format='%08d%s'):
        super(FrameStore, self).__init__(root)
        self._root = root
        self._extension = extension
        self._frame_filename_format = frame_filename_format

    @property
    def root(self):
        return self._root

    @property
    def extension(self):
        return self._extension

    @property
    def frame_filename_format(self):
        return self._frame_filename_format

    @lru_cache(maxsize=128)
    def get_frame(self, video, frame_index, modality=Modality.RGB, timestamp=''):
        frame_path = self.get_frame_path(video, modality, frame_index)
        frame_img = Image.open(frame_path)

        return Frame(frame_img, modality, index=frame_index, source_video=video, timestamp=timestamp)

    def get_frames(self, video, frame_indices, modality=Modality.RGB):
        return [self.get_frame(video, frame_index, modality) for frame_index in frame_indices]

    def get_frame_sequence(self, video, frame_range: TemporalRange, modality=Modality.RGB):
        return self.get_frames(video, range(frame_range.start_frame, frame_range.end_frame + 1), modality)

    def get_frame_path(self, video, modality, frame_index):
        frame_filename = self.get_frame_filename(frame_index)
        return os.path.join(self.root, video, modality.name, frame_filename)

    def get_frame_filename(self, frame_index):
        return self._frame_filename_format % (frame_index, self._extension)

    def load_image_for_frame(self, frame: Frame, func):
        frame = self.get_frame(frame.source_video, frame.index, frame.modality, frame.timestamp)
        return func(frame)
