// ===============================
// SOCIAL MEDIA AI DETECTOR
// content.js
// ===============================

/**
 * Sends an image URL to the FastAPI backend
 */
async function analyzeImage(imageUrl) {

    return new Promise((resolve) => {

        chrome.runtime.sendMessage(
            {
                type: "analyze",
                imageUrl: imageUrl
            },

            (response) => {

                if (chrome.runtime.lastError) {

                    console.error(chrome.runtime.lastError);

                    resolve(null);

                    return;
                }

                console.log("Backend Response:", response);

                resolve(response?.authenticity_score ?? null);

            }

        );

    });

}

/**
 * Creates a badge on a post if it doesn't already exist
 */
function createBadge(post) {

    let badge = post.querySelector(".ai-detector-badge");

    if (badge) return badge;

    badge = document.createElement("div");

    badge.className = "ai-detector-badge";

    badge.innerText = "🤖 Authenticity Score: Analyzing...";

    badge.style.position = "absolute";
    badge.style.top = "10px";
    badge.style.left = "10px";
    badge.style.background = "#ff3040";
    badge.style.color = "white";
    badge.style.padding = "8px 12px";
    badge.style.borderRadius = "8px";
    badge.style.fontSize = "12px";
    badge.style.fontWeight = "bold";
    badge.style.zIndex = "999999";

    post.style.position = "relative";

    post.appendChild(badge);

    return badge;
}

/**
 * Scan Instagram posts
 */
function scanPosts() {

    const posts = document.querySelectorAll("article");

    console.log("Posts Found:", posts.length);

    for (const post of posts) {

        // Skip already analyzed posts
        if (post.dataset.aiAnalyzed === "true") {
            continue;
        }

        const img = post.querySelector("img");

        if (!img) {
            continue;
        }

        // Mark as analyzed immediately
        post.dataset.aiAnalyzed = "true";

        const badge = createBadge(post);

        analyzeImage(img.src).then(score => {
            console.log("Score:", score);

            if (score !== null) {

                badge.innerText =
                    `🤖 Authenticity Score: ${score}%`;

            } else {

                badge.innerText =
                    "⚠️ Analysis Failed";
            }
        });
    }
}

// Initial scan
scanPosts();

// Scan every 5 seconds for newly loaded posts
setInterval(scanPosts, 5000);