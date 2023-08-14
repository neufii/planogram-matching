import torch
from .config import MODEL_WEIGHT, CONFIDENCE

#YOLOv5 Version

def load_model():
   # Load a model
   model = torch.hub.load('ultralytics/yolov5', 'custom', MODEL_WEIGHT)  # custom trained model
   model.conf = CONFIDENCE

   return model

def detect(model, img_path):
   # Inference
   results = model(img_path)
   prediction = results.pandas().xyxy[0]

   return prediction