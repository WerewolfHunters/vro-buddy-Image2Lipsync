import requests
import os
import time
from dotenv import load_dotenv

class Lipsync:
    def __init__(self):
        load_dotenv()
        self.api_key = os.environ.get("HEYGEN_API_KEY")
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "x-api-key": self.api_key
        }

    def upload_image(self, image_path: str) -> str:
        """Upload image and return talking_photo_id"""
        with open(image_path, "rb") as f:
            resp = requests.post(
                "https://upload.heygen.com/v1/talking_photo",
                data=f,
                headers={"Content-Type": "image/jpeg", "x-api-key": self.api_key}
            )
        data = resp.json()
        return data["data"]["talking_photo_id"]

    def generate_video(self, talking_photo_id, text, language, gender, output_filename="generated_video.mp4"):
        url = "https://api.heygen.com/v2/video/generate"

        # Pick a voice_id based on language/gender (placeholder values for now)
        voice_map = {
            ("eng", "male"): "d7bbcdd6964c47bdaae26decade4a933",
            ("eng", "female"): "73c0b6a2e29d4d38aca41454bf58c955",
            ("hin", "male"): "2fc30cb6995f458ca73ae87e3a74d644",
            ("hin", "female"): "3240f8ee6b06414cb9bab4f9615445af",
        }
        voice_id = voice_map.get((language, gender), "d7bbcdd6964c47bdaae26decade4a933")

        payload = {
            "video_inputs": [
                {
                    "character": {
                        "type": "talking_photo",
                        "talking_photo_id": talking_photo_id
                    },
                    "voice": {
                        "type": "text",
                        "input_text": text,
                        "voice_id": voice_id
                    },
                    "background": {
                        "type": "color",
                        "value": "#FAFAFA"
                    }
                }
            ],
            "dimension": {
                "width": 1280,
                "height": 720
            }
        }

        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "x-api-key": self.api_key
        }

        # First request to generate video
        response = requests.post(url, json=payload, headers=headers)
        job_data = response.json()["data"]
        video_id = job_data["video_id"]
        print(f"🎬 Video generation started with ID: {video_id}")

        # Poll status until completed
        status_url = f"https://api.heygen.com/v1/video_status.get?video_id={video_id}"
        while True:
            status_resp = requests.get(status_url, headers=headers).json()
            status = status_resp["data"]["status"]

            if status == "completed":
                video_url = status_resp["data"]["video_url"]
                print(f"✅ Video generation completed: {video_url}")

                # Save video
                video_content = requests.get(video_url).content
                with open(output_filename, "wb") as f:
                    f.write(video_content)
                return output_filename

            elif status in ["processing", "waiting", "pending"]:
                print("⏳ Video still processing... checking again in 5s")
                time.sleep(5)
            else:
                raise Exception(f"Video generation failed: {status_resp}")

