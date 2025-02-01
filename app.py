from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
import os
# Load environment variables
load_dotenv()
# Load the model and get responses
def get_gemini_response(question):
    llm = ChatGoogleGenerativeAI(
        google_api_key=os.getenv("GEMINI_API_KEY"),  
        model="gemini-pro",  
        temperature=0.5  
    )
    response = llm.predict(question)  
    return response
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")
input = st.text_input("Input:", key="input")
submit = st.button("Ask the question")
if submit:
    st.subheader("The Response is:")
    response = get_gemini_response(input)  
    st.write(response)