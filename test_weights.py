import torch

ckpt = torch.load(
    "UniversalFakeDetect/pretrained_weights/fc_weights.pth",
    map_location="cpu"
)

print(type(ckpt))

if isinstance(ckpt, dict):
    print(ckpt.keys())