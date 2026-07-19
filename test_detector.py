from PIL import Image

from backend.detector.preprocess import preprocess
from backend.detector.detector import AIDetector

# Load detector
detector = AIDetector()

# Load image
image = Image.open("test.jpg").convert("RGB")

# Preprocess
tensor = preprocess(image)

# Predict
score = detector.predict(tensor)

print(f"Authenticity Score: {score}%")