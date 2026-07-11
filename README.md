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

- **Browser Extension**: Initial setup with `manifest.json`, `content.js`, and `styles.css` is complete. 
- **Backend API**: A basic FastAPI backend has been established. Currently, it exposes an `/analyze` endpoint that returns a mock authenticity score (between 40 and 95) for testing the integration with the extension.
- **Next Steps**: Integrate the actual AI detection model in the backend and refine the content script to robustly handle dynamic Instagram DOM updates.