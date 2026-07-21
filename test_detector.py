from pathlib import Path
from PIL import Image

from backend.detector.preprocess import preprocess
from backend.detector.detector import AIDetector


def test_image(detector, image_path):

    print("\n" + "=" * 60)
    print(f"Testing: {image_path.name}")
    print("=" * 60)

    # Load image
    image = Image.open(image_path).convert("RGB")
    print("Image size:", image.size)

    # Preprocess
    tensor = preprocess(image)
    print("Tensor shape:", tensor.shape)
    print("Tensor dtype:", tensor.dtype)

    # Predict
    print("Running prediction...")

    try:
        score = detector.predict(tensor)

        print("Prediction successful!")

        # Temporary assumption:
        # score >= 50 => AI
        # score < 50 => Real
        prediction = "AI Generated" if score >= 50 else "Real"

        print(f"Prediction         : {prediction}")
        print(f"Authenticity Score : {score}%")

    except Exception:
        import traceback
        traceback.print_exc()


def main():

    print("Step 1: Creating detector...")
    detector = AIDetector()

    project_root = Path(__file__).parent

    test_images = [
        project_root/ "test.jpg",
        project_root / "AI_image.png"
    ]

    for image_path in test_images:

        if image_path.exists():
            test_image(detector, image_path)
        else:
            print(f"\n❌ {image_path.name} not found.")


if __name__ == "__main__":
    main()