import os
import io
import requests
import streamlit as st
# from huggingface_hub import InferenceClient

from PIL import Image
from datetime import datetime

def text_to_image(prompt: str):
    
    #from huggingface_hub import InferenceClient
    #client = InferenceClient("stabilityai/stable-diffusion-3.5-large", token="hf_xxxxxxx")

    # output is a PIL.Image object
    #image = client.text_to_image(prompt)


    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3.5-large"
    headers = {"Authorization": "Bearer hf_xxxxxxx"}

    def query(payload):
	    response = requests.post(API_URL, headers=headers, json=payload)
	    return response.content

    image_bytes = query({
	    "inputs": prompt,
    })

    # You can access the image with PIL.Image for example
    image = Image.open(io.BytesIO(image_bytes))

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}.JPG"

    # Get the directory of the current Python script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the full file path
    file_path = os.path.join(script_dir, filename)

    image.save(file_path)
    return file_path


def main():
    st.title("Text to Image Generator")
    prompt = st.text_input("Enter a text prompt to generate an image:")
    if st.button("Generate Image"):
        if prompt:
            image_path = text_to_image(prompt)
            st.image(image_path, caption=prompt)
        else:
            st.error("Please enter a text prompt.")

if __name__ == "__main__":
    main()

