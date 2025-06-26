import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI



st.title("Ask me Anything")
with st.sidebar:
    st.title("Provide your api key")
    api_key=st.text_input("api_key",type="password")
if not api_key:
    st.info("Enter api key to proceed")
    st.stop()

llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=api_key)
question=st.text_input("Enter the question")
if question:
    response=llm.invoke(question)
    st.write(response.content)
