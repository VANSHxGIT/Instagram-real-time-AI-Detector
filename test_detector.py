from PIL import Image
import torch

from backend.detector.preprocess import preprocess
from backend.detector.detector import AIDetector

print("Step 1: Creating detector...")
detector = AIDetector()

print("Step 2: Loading image...")
image = Image.open("test.jpg").convert("RGB")
print("Image size:", image.size)

print("Step 3: Preprocessing...")
tensor = preprocess(image)

print("Tensor shape:", tensor.shape)
print("Tensor dtype:", tensor.dtype)

print("Step 4: Running prediction...")

try:
    score = detector.predict(tensor)
    print("Prediction successful!")
    print(f"Authenticity Score: {score}%")

except Exception as e:
    import traceback
    traceback.print_exc()