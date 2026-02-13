import os
import requests
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__,
            template_folder="../frontend/templates",
            static_folder="../frontend/static")

CORS(app)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_video():
    data = request.get_json()
    prompt = data.get("prompt")

    try:
        response = requests.post(
            "https://generativelanguage.googleapis.com/v1beta/models/veo-3:generateVideo",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {GEMINI_API_KEY}"
            },
            json={
                "prompt": prompt,
                "aspectRatio": "16:9",
                "durationSeconds": 8
            }
        )

        result = response.json()

        # This depends on actual Veo response structure
        video_url = result.get("videoUrl")

        return jsonify({"videoUrl": video_url})

    except Exception as e:
        print(e)
        return jsonify({"error": "Video generation failed"}), 500


if __name__ == "__main__":
    app.run(debug=True)