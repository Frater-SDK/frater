import os
from dataclasses import dataclass

from PIL import Image

from .file_store import FileStore, FileStoreConfig
from ...utilities.image import load_image_from_url, load_image_from_file, save_image_to_file
from ...utilities.url import is_url


@dataclass
class ImageStoreConfig(FileStoreConfig):
    name: str = 'image_store_config'


class ImageStore(FileStore):
    def __init__(self, root):
        super(ImageStore, self).__init__(root)

    def load_image(self, image_path: str) -> Image.Image:
        if is_url(image_path):
            return load_image_from_url(image_path)

        if os.path.isfile(image_path):
            return load_image_from_file(image_path)

        full_path = self.get_full_path(image_path)
        if os.path.isfile(full_path):
            return load_image_from_file(full_path)
        else:
            raise FileNotFoundError(f'Unable to find image at {full_path}')

    def save_image(self, image: Image.Image, image_path: str):
        if os.path.isdir(os.path.dirname(image_path)):
            save_image_to_file(image, image_path)
        else:
            full_path = self.get_full_path(image_path)
            save_image_to_file(image, full_path)
