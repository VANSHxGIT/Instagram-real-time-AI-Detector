import requests
from PIL import Image
from io import BytesIO


def download_image(url):

    response = requests.get(url, timeout=20)

    response.raise_for_status()

    image = Image.open(BytesIO(response.content)).convert("RGB")

    return image