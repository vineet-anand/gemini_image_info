#### Loading Environment Variables

from dotenv import load_dotenv
load_dotenv()

#### Importing Libraries

import os
import streamlit as st
from PIL import Image
import google.generativeai as genai

genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

#### Function to load model and get response

def get_response(input, image):
    if input != "":
        response = model.generate_content([input, image])

    else:
        response = model.generate_content(image)
        
    return response.text

##### Streamlit Frontend to display response

st.set_page_config(page_title= "Gemini Image Testing")

st.header("Gemini Application")

input = st.text_input("Input Prompt: ", key="input")

upload_file = st.file_uploader("Choose an Image...", type= ["jpg", "jpeg", "png"])
image = ""

if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image, caption="Upload Image.", use_column_width= True)

submit = st.button("Tell me about Image")

if submit:
    response = get_response(input, image)
    st.subheader("The response is: ")
    st.write(response)
