from fastapi import FastAPI
from pydantic import BaseModel
from backend.downloader import download_image
from backend.detector.preprocess import preprocess
from backend.detector.detector import AIDetector

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