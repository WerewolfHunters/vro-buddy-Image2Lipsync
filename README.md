# 🗣️ Image-to-Video Lip Sync Generator

This project allows you to generate lip-synced videos from a static image and custom script using the **HeyGen API**.  
It includes a **Streamlit UI** for easy interaction where you can:

- Upload an image
- Enter your script
- Select language (`eng` / `hin`)
- Select voice gender (`male` / `female`)
- Generate and view the resulting video directly in the browser

For video demo: [click here](https://drive.google.com/file/d/1X-sStm1hWVksRlZECMDxCLwZyLuhVBO5/view?usp=sharing)
---

## 🚀 Features
- Simple **Streamlit web app**
- Upload image + custom script
- Choose language & gender for voice
- Video generated & displayed in the UI
- API calls handled via an OOP-based `Lipsync` class
- Dockerized for easy deployment

---

## 🛠️ Local Setup (Python Virtual Environment)

### 1. Clone the repository
```bash
git clone https://github.com/WerewolfHunters/vro-buddy-Image2Lipsync.git
cd vro-buddy-Image2Lipsync
```

### 2. Create and activate virtual environment
- Create venv
```bash
python -m venv venv
```

- Activate venv
1) On Windows
```bash
venv\Scripts\activate
```
2) On macOS/Linux
```bash
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set your API key
Export your HeyGen API Key in the `.env` file:
```bash
HEYGEN_API_KEY="your_api_key"
```
Refer this doc: [click here](https://docs.google.com/document/d/1h1udFsGgkmIPpE8Xb6zC3hXNo2r8jPkvlVj81HyoNZc/edit?usp=sharing) to get your heygen_api_key

### 5. Run the Streamlit app
```bash
streamlit run main.py
```
Now open 👉 http://localhost:8501

---

## 🐳 Run with Docker

### 1. Build the Docker image
```bash
docker build -t lipsync-app .
```

### 2. Run the container
```bash
docker run -p 8501:8501 --env HEYGEN_API_KEY=your_api_key_here lipsync-app
```
Open 👉 http://localhost:8501

---

## 📂 Project Structure
```bash
.
├── main.py                   # Streamlit app entry point
├── heygen_lipsync_oops.py    # Lipsync class (OOP implementation)
├── requirements.txt          # Python dependencies
├── Dockerfile                # Docker configuration
└── README.md                 # Project documentation
```

---

## 🔮 Future Plans
- Explore other AI video & audio tools to enhance customization
- Support for multi-speaker dialogues
- Add voice cloning features
- Deploy on cloud platforms (Render, AWS, Hugging Face Spaces)
- Build an API wrapper for programmatic video generation

---

## 🤝 Contributing
Pull requests are welcome! Please open an issue first to discuss any major changes.

---

## 📜 License
This project is licensed under the MIT License.


