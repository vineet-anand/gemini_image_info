#### Loading Environment Variables

from dotenv import load_dotenv
load_dotenv()

#### Importing all Libraries

import os
import streamlit as st
import google.generativeai as genai

genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

#### Function to load model and get response

def get_response(question):
    response = model.generate_content(question)
    return response.text

##### Streamlit Frontend to display response

st.set_page_config(page_title="Gemini Q&A")
st.header("Gemini LLM App")

input = st.text_input("Input: ", key="input")
submit = st.button("Ask any question")

if submit:
    response = get_response(input)
    st.subheader("The response is: ")
    st.write(response)

