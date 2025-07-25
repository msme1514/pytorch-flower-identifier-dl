import torch
from torchvision import models, transforms
from PIL import Image
import json
import os

# Load flower metadata
def load_catalog(path="./flower_catalog.json"):
    with open(path, 'r') as f:
        return json.load(f)

# Image preprocessing
def preprocess_image(image):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])
    return transform(image).unsqueeze(0)

# Load model
def load_model(model_path="model/flower_classifier_resnet18.pth"):
    model = models.resnet18(pretrained=False)
    model.fc = torch.nn.Linear(model.fc.in_features, 102)
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    model.eval()
    return model

# Predict flower class
def predict(image, model, catalog):
    input_tensor = preprocess_image(image)
    with torch.no_grad():
        output = model(input_tensor)
        _, predicted = torch.max(output, 1)
        class_idx = str(predicted.item())
        return catalog.get(class_idx, {"name": "Unknown", "price": "-", "available": False, "care": "N/A"})
