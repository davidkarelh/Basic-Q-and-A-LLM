import streamlit as st
from langchain_helper import create_vector_db, get_qa_chain
import re

st.title("Q and A LLM System")

question = st.text_input("Question: ")

if question:
    chain = get_qa_chain()
    response = chain(question)
    st.header("Answer: ")
    # st.write(response["result"])
    st.write(re.sub(r'.*?Answer:', '', response["result"]))