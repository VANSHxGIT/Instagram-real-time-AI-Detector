from fastapi import FastAPI
from pydantic import BaseModel
from downloader import download_image
from preprocess import preprocess
from detector import AIDetector

app = FastAPI()
detector = AIDetector()

class ImageRequest(BaseModel):
    image_url: str

@app.post("/analyze")
def analyze(req: ImageRequest):

    image = download_image(req.image_url)

    tensor = preprocess(image)

    score = detector.predict(tensor)

    return {
        "authenticity_score": score
    }