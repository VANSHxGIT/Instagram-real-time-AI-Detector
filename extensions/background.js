chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {

    console.log("Received request:", request);

    if (request.type !== "analyze") {
        return;
    }

    fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            image_url: request.imageUrl
        })
    })
        .then(async (response) => {

            console.log("Response status:", response.status);

            const data = await response.json();

            console.log("Response data:", data);

            sendResponse(data);
        })
        .catch((error) => {

            console.error("Fetch failed:", error);

            sendResponse({
                authenticity_score: null
            });
        });

    return true;
});