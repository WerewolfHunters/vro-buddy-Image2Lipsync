import streamlit as st
import os
from heygen_lipsync import Lipsync

st.set_page_config(page_title="Lipsync Video Generator", layout="centered")

st.title("🎥 Lipsync Video Generator")

# Upload Image
uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

# Script
script = st.text_area("Enter your script", placeholder="Type the text you want the avatar to say...")

# Language
language = st.selectbox("Select Language", ["eng", "hin"])

# Gender
gender = st.selectbox("Select Gender", ["male", "female"])

# Generate button
if st.button("Generate"):
    if uploaded_image and script.strip():
        # Save uploaded image temporarily
        img_path = os.path.join("temp_image.jpg")
        with open(img_path, "wb") as f:
            f.write(uploaded_image.read())

        # Run lipsync
        lipsync = Lipsync()
        talking_id = lipsync.upload_image(img_path)
        output_path = lipsync.generate_video(talking_id, script, language, gender, "generated_output.mp4")

        st.success("✅ Video generated successfully!")
        st.video(output_path)

    else:
        st.error("⚠️ Please upload an image and enter a script before generating.")
