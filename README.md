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