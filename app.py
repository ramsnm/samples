import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
genai.configure(api_key="")
model=genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input, image, prompt):
    response=model.generate_content([input, image[0], prompt])
    return response.text

def image_input_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type" : uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("File does not exist")
    
import streamlit as st
st.set_page_config(page_title="Ramesh first LLM project")

st.header("Ramesh LLM application")

input=st.text_input("Input prompt:", key="input")

uploaded_file = st.file_uploader("Choose a image to process .. ", type=["jpg","jpeg","png"])

image=""

if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image, caption="Uploaded file ", use_column_width=True)

submit = st.button("Tell me about the image")

input_prompt = """
    You are an expert in understanding invoices. we will upload a image as invoice
    and you have to answer any questions based on the uploaded invoice image
"""

if submit:
    image_data = image_input_setup(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("The response is")
    st.write(response)
