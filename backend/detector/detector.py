from pathlib import Path
import torch

from UniversalFakeDetect.models import get_model


class AIDetector:
    def predict(self, tensor):

        with torch.no_grad():

            tensor = tensor.to(self.device)

            logits = self.model(tensor)

        probability = torch.sigmoid(logits).item()

        return round(probability * 100, 2)

    def __init__(self):

        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu"
        )

        print(f"Using device: {self.device}")

        print("Loading UnivFD model...")

        # Load CLIP backbone
        self.model = get_model("CLIP:ViT-L/14")

        # Project root
        ROOT = Path(__file__).resolve().parents[2]

        weights_path = (
            ROOT
            / "UniversalFakeDetect"
            / "pretrained_weights"
            / "fc_weights.pth"
        )

        classifier = torch.load(
            weights_path,
            map_location=self.device
        )

        self.model.fc.load_state_dict(classifier)

        self.model.to(self.device)

        self.model.eval()

        print("✅ UnivFD loaded successfully")