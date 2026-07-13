import requests
from PIL import Image
from io import BytesIO

session = requests.Session()
session.headers.update({"User-Agent": "Mozilla/5.0"})


def download_image(url: str):

    response = session.get(
        url,
        timeout=10
    )

    response.raise_for_status()

    return Image.open(BytesIO(response.content)).convert("RGB")