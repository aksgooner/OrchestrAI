import os
import streamlit as st
from utils.summarize import summarize_pdf
import openai

# Set up OpenAI API key
# Retrieve the OpenAI API key from an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")
#streamlit App
st.title("OrchestrAI - Research Paper Summarizer")

#Upload a file
uploaded_file = st.file_uploader("Uploade a PDF file", type = ["pdf"])

if uploaded_file is not None:
    #save uploaded file to a temp location
    temp_path = os.path.join("data",uploaded_file.name)
    
    with open(temp_path,"wb") as f:
        f.write(uploaded_file.read())

    #summarize button
    if st.button("Summarize"):
        with st.spinner("Summarizing..."):
            summary= summarize_pdf(temp_path)

        #Display Summary
        st.subheader("Summary")
        st.text_area("Summary of PDF", summary, height=500)