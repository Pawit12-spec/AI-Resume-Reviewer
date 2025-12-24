import dotenv
import numpy as np
import streamlit as st
import PyPDF2 
import io
from openai import OpenAI
import os
from dotenv import load_dotenv

#import API key saved in a .env file
load_dotenv()
OPEN_API_KEY = os.getenv("API_KEY")

#create basic UI using streamlit library
st.set_page_config(page_title= " AI Resume Reviewer", page_icon= "📝", layout = "centered")
st.title("AI Resume Reviewer.")
st.markdown("Upload you resume for a AI review")
#provide ability to upload file via streamlit
uploaded_file = st.file_uploader("upload your resume (PDF or TXT)", type=["pdf", "txt"])


job_role = st.text_input("Enter the job role you're targetting (optional)")

analyse = st.button("Analyse Resume")


def extract_text_from_pdf(pdf_file):
    """ 
    return the content of a pdf file
        Parameters:
                pdf_file(file): a pdf file
            
        Returns:
                txt (str): string of texts of content from the pdf file
        """
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text
    
    
def extract_text(uploaded_file):
    """
    Return decoded content of pdf file
        parameters:
                uploaded_file(file): uploaded pdf file
        Returns:
                str = string of contents from uplaoded file whether pdf or a .txt file
    """
    
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")
    
# check requirements
if analyse and uploaded_file:
    try: 
        file_content = extract_text(uploaded_file)
        
        if not file_content.strip():
            st.error("File does not have content...")
            st.stop()
            
        
        #prompt designed for our requirement   
        prompt = f""" Please analyse this resume and provide constructive feedback.
        focus on the following aspects:
        1. content and clarity
        2. skills presentation
        3. Experience description
        4. Specific improvements for {job_role if job_role else 'general job applications'}
        
        resume content: {file_content}
        
        please provide your analysis in a clear structured format with specific recommendations"""
        
        

        # get response from LLM model (can be changed based on user preference such as Grok, Gemini etc)
        client = OpenAI(api_key= OPEN_API_KEY)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
               { "role": "system", "content": "you are an expert resume reviewer with years of experience"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
        )
        
        st.markdown("Analysis Review and Feedback")
        st.markdown(response.choices[0].message.content)
    

    except Exception as e:
        st.error(e)
