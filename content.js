function addBadge() {

    const posts = document.querySelectorAll("article");

    posts.forEach(post => {

        if (post.querySelector(".ai-detector-badge")) {
            return;
        }

        const badge = document.createElement("div");

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
    });
}

setInterval(addBadge, 2000);
function getImages() {

    const images = document.querySelectorAll("article img");

    console.log("Images Found:", images.length);

    images.forEach(img => {
        console.log(img.src);
    });
}

setInterval(getImages, 5000);
async function analyzeImage(imageUrl) {

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/analyze",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    image_url: imageUrl
                })
            }
        );

        const data = await response.json();

        console.log("Backend Response:", data);

        return data.authenticity_score;

    } catch (error) {

        console.error("API Error:", error);

        return null;
    }
}
const posts = document.querySelectorAll("article");

posts.forEach(async (post) => {

    const img = post.querySelector("img");

    if (!img) return;

    const score = await analyzeImage(img.src);

    console.log("Score:", score);

});