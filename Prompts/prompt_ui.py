from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header("Reasearch Paper Summarizer")

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro")

user_input = st.text_input("Enter the research paper text here")

if st.button("Summarize"):
    result = model.invoke(user_input)
    st.write(result.content)