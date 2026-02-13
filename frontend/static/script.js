async function generateVideo() {

    const prompt = document.getElementById("prompt").value;
    const status = document.getElementById("status");
    const video = document.getElementById("outputVideo");

    if (!prompt) {
        alert("Please enter a prompt!");
        return;
    }

    status.innerText = "Generating video... ⏳";

    try {
        const response = await fetch("/generate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ prompt })
        });

        const data = await response.json();

        if (data.videoUrl) {
            video.src = data.videoUrl;
            status.innerText = "Video Generated Successfully 🎉";
        } else {
            status.innerText = "Failed to generate video.";
        }

    } catch (error) {
        console.error(error);
        status.innerText = "Error generating video.";
    }
}
