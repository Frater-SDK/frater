from io import BytesIO

import requests
from PIL import Image


def load_image_from_file(filename):
    return Image.open(filename)


def save_image_to_file(image: Image.Image, filename):
    image.save(filename)


def load_image_from_url(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))
