import requests
from PIL import Image
from io import BytesIO


def download_image(url: str):

    response = requests.get(
        url,
        headers={
            "User-Agent":
            "Mozilla/5.0"
        },
        timeout=10
    )

    response.raise_for_status()

    return Image.open(BytesIO(response.content)).convert("RGB")