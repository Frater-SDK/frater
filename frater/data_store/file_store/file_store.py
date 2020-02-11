import os
from dataclasses import dataclass

from ...config import Config
from ...utilities import Singleton


@dataclass
class FileStoreConfig(Config):
    name: str = 'file_store_config'
    root: str = ''


class FileStore(metaclass=Singleton):
    def __init__(self, config: FileStoreConfig):
        self.config = config

    @property
    def root(self):
        return os.path.abspath(os.path.expandvars(os.path.expanduser(self.config.root)))

    def get_full_path(self, file_path):
        return os.path.join(self.root, file_path)
