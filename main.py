from fastapi import FastAPI
from pydantic import BaseModel
import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ImageRequest(BaseModel):
    image_url: str

@app.post("/analyze")
def analyze_image(data: ImageRequest):

    score = random.randint(40, 95)

    return {
        "authenticity_score": score
    }