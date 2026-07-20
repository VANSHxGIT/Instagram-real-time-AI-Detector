# Instagram Real-Time AI Detector

This project is a browser extension and backend service designed to detect AI-generated images on Instagram in real-time.

## Architecture Pipeline

```text
Instagram Feed
       │
       ▼
Browser Extension (Content Script)
       │
       ▼
Detect <article> posts
       │
       ▼
Extract Image URL
       │
       ▼
Background Service Worker
       │
       ▼
FastAPI Backend
       │
       ▼
Return Authenticity Score
       │
       ▼
Overlay Badge
```

## Progress (As of 11 July 2026)

![development plan as of 11 july 2026](Development%20-%2011July26.png)

- **Browser Extension**: Initial setup with `manifest.json`, `content.js`, and `styles.css` is complete. 
- **Backend API**: A basic FastAPI backend has been established. Currently, it exposes an `/analyze` endpoint that returns a mock authenticity score (between 40 and 95) for testing the integration with the extension.
- **Next Steps**: Integrate the actual AI detection model in the backend and refine the content script to robustly handle dynamic Instagram DOM updates.

## Our Immediate Next Goal

We'll first get real image detection working. Once that's stable, we can add the other modalities one by one.

Phase 3 Roadmap:
1. Integrate a pretrained detector (replace placeholder scores).
2. Run inference on Instagram images.
3. Return actual AI probabilities.
4. Display real scores in the extension.
5. Optimize inference speed and caching.


#  Development Progress Log

##  Development Timeline

### 11 July 2026 — Phase 1: Browser Extension Foundation

Successfully built the initial Chrome extension for Instagram.

### Achievements
- Created the extension using Manifest V3.
- Integrated the extension with Instagram pages.
- Implemented automatic scanning of Instagram posts.
- Extracted images from each post.
- Added an overlay badge displaying:
  > 🤖 Authenticity Score: Analyzing...
- Established the basic project structure.
- Set up the FastAPI backend.

---

### 12–15 July 2026 — Backend Communication

Focused on connecting the extension with the backend server.

### Achievements
- Created the `/analyze` API endpoint.
- Implemented image downloading from Instagram URLs.
- Fixed CORS issues.
- Resolved HTTP `OPTIONS` (405) errors.
- Successfully enabled communication between:
  - Browser Extension
  - FastAPI Backend
- Returned dummy authenticity scores for testing.

---

### 16–18 July 2026 — AI Model Integration

Integrated the Universal Fake Image Detector (UnivFD).

### Achievements
- Added the UnivFD repository to the project.
- Integrated the CLIP ViT-L/14 backbone.
- Loaded the pretrained classifier (`fc_weights.pth`).
- Implemented:
  - Image preprocessing
  - Tensor conversion
  - Model loading
  - Inference pipeline
- Created a reusable `AIDetector` class.

---

### 19 July 2026 — Debugging & Environment Setup

Resolved multiple integration and dependency issues.

### Major Fixes
- Fixed Python environment inconsistencies.
- Switched project to Python 3.11 for compatibility.
- Resolved:
  - Missing `pkg_resources`
  - Missing `tqdm`
  - Missing `Pillow`
  - Missing `torchvision`
- Fixed import path issues.
- Fixed circular import errors.
- Successfully initialized the UnivFD model.

---

### 20 July 2026 — First Successful AI Inference 🎉

Reached the first complete end-to-end AI inference milestone.

### Achievements
- Successfully loaded the pretrained UnivFD model.
- Verified image preprocessing pipeline.
- Executed inference on a real image.
- Generated authenticity predictions from the neural network.
- Confirmed:
  - Image Loading ✅
  - Tensor Preprocessing ✅
  - CLIP Feature Extraction ✅
  - Neural Network Inference ✅
  - Authenticity Score Generation ✅

Example Output:

```text
Using device: cpu
Loading UnivFD model...
✅ UnivFD loaded successfully

Image size: (8064, 6048)
Tensor shape: torch.Size([1, 3, 224, 224])

Logits: tensor([[-12.3482]])

Prediction successful!
Authenticity Score: 0.0%
```

---

# Current Project Status (20 July 2026)

## Completed
- Browser Extension
- Instagram Integration
- FastAPI Backend
- Image Downloader
- Image Preprocessing
- UnivFD Integration
- CLIP ViT-L/14 Model Loading
- Pretrained Weight Loading
- Neural Network Inference
- Authenticity Score Generation

## In Progress
- Connect real UnivFD predictions to the browser extension.
- Verify AI/Real label mapping.
- Improve prediction confidence calibration.
- Optimize inference speed.

## Upcoming Features
- Real-time AI detection while scrolling.
- Color-coded authenticity badges.
- Support for additional social media platforms.
- Batch inference and prediction caching.
- Explainable AI insights (heatmaps and confidence explanations).
- Custom fine-tuned detection model.
