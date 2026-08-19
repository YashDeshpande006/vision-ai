# 🔍 Vision AI — Intelligent Image Analysis

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-FF4081?style=for-the-badge)
![BLIP](https://img.shields.io/badge/BLIP-Salesforce-4A90D9?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**A real-time image analysis web application combining object detection and AI-generated scene captioning.**

[Features](#-features) · [Getting Started](#-getting-started) · [API Reference](#-api-reference) · [Tech Stack](#-tech-stack)

</div>

---

## ✨ Features

- 🎯 **Object Detection** — Powered by [YOLOv8](https://github.com/ultralytics/ultralytics), detects and counts objects in any uploaded image
- 📝 **Scene Captioning** — Uses [BLIP](https://huggingface.co/Salesforce/blip-image-captioning-base) (Bootstrapped Language-Image Pre-training) to generate natural language descriptions of images
- ⚡ **REST API** — FastAPI backend with a clean `/analyze-image` endpoint
- 🌐 **Interactive UI** — Drag-and-drop HTML interface to upload images and view results instantly
- 🔓 **CORS Enabled** — Ready to integrate with any frontend framework

---



## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/vision-ai.git
   cd vision-ai
   ```

2. **Create a virtual environment** *(recommended)*
   ```bash
   python -m venv venv
   source venv/bin/activate       # Linux/macOS
   venv\Scripts\activate          # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   > 📦 The YOLOv8 model weights (`yolov8n.pt`) will be **automatically downloaded** by `ultralytics` on first run. The BLIP model will be auto-downloaded from HuggingFace.

4. **Run the server**
   ```bash
   uvicorn vision_api:app --reload
   ```
   Server starts at: `http://localhost:8000`

5. **Open the UI**
   
   Open `image-analysis-ui.html` in your browser.

---

## 📡 API Reference

### `GET /`
Health check endpoint.

**Response:**
```json
{ "message": "Image Analysis API is running" }
```

---

### `POST /analyze-image`
Analyze an uploaded image for object detection and scene captioning.

**Request:** `multipart/form-data`
| Field | Type | Description |
|-------|------|-------------|
| `file` | `UploadFile` | Image file (JPEG, PNG, etc.) |

**Response:**
```json
{
  "scene_description": "string",
  "objects_detected": [
    { "object": "string", "count": "integer" }
  ]
}
```

**Error Response:**
```json
{ "error": "error message" }
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | [FastAPI](https://fastapi.tiangolo.com/) + [Uvicorn](https://www.uvicorn.org/) |
| **Object Detection** | [YOLOv8n](https://github.com/ultralytics/ultralytics) (Ultralytics) |
| **Image Captioning** | [BLIP](https://huggingface.co/Salesforce/blip-image-captioning-base) (Salesforce / HuggingFace) |
| **Image Processing** | [Pillow](https://pillow.readthedocs.io/) |
| **Deep Learning** | [PyTorch](https://pytorch.org/) |
| **Frontend** | Vanilla HTML/CSS/JS |

---

## 📁 Project Structure

```
vision-ai/
├── vision_api.py           # FastAPI backend — detection & captioning logic
├── image-analysis-ui.html  # Frontend web interface
├── requirements.txt        # Python dependencies
└── README.md
```

---

## 🎓 About

This project was built as part of **Project Exhibition 2** of the B.Tech. Computer Science and Engineering program. It demonstrates the integration of two state-of-the-art computer vision models into a unified, production-ready REST API.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
