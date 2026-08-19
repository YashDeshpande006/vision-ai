from fastapi import FastAPI, File, UploadFile
from PIL import Image
import io
from collections import Counter
from fastapi.middleware.cors import CORSMiddleware
from ultralytics import YOLO

from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

app = FastAPI(title="Image Analysis API") # INITIALIZE APP

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

print("Loading YOLO model...") # LOAD MODELS 
yolo_model = YOLO("yolov8n.pt")

print("Loading BLIP model...")
blip_processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)
blip_model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

print("Models loaded successfully!")

def read_image(file_bytes): # HELPER FUNCTIONS
    """Convert uploaded file to PIL image"""
    image = Image.open(io.BytesIO(file_bytes)).convert("RGB")
    return image


def detect_objects(image):
    """Run YOLO object detection and count objects"""
    results = yolo_model(image)
    detections = results[0].boxes

    if detections is None or len(detections) == 0:
        return []

    class_ids = detections.cls.tolist()
    names = yolo_model.names

    labels = [names[int(cls_id)] for cls_id in class_ids]
    counts = Counter(labels)

    return [
        {"object": obj, "count": count}
        for obj, count in counts.items()
    ]


def generate_caption(image):
    """Generate image caption using BLIP"""
    inputs = blip_processor(image, return_tensors="pt")
    output = blip_model.generate(**inputs)
    caption = blip_processor.decode(output[0], skip_special_tokens=True)
    return caption

@app.get("/") # API ROUTES
def home():
    return {"message": "Image Analysis API is running"}


@app.post("/analyze-image")
async def analyze_image(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = read_image(contents)

        objects = detect_objects(image)
        caption = generate_caption(image)

        return {
            "scene_description": caption,
            "objects_detected": objects
        }

    except Exception as e:
        return {
            "error": str(e)
        }



