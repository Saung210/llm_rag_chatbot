import streamlit as st
from rag import retrieve
from llm import ask_llm

st.title("🎓 RAI KMITL Chatbot")
st.write("Ask anything about the Robotics & AI Engineering program")

question = st.text_input("Enter your question:")

if question:
    st.write("🔍 Searching knowledge base...")

    context = retrieve(question)

    st.write("🤖 Generating answer...")

    answer = ask_llm(question, context)

    st.subheader("Answer")
    st.write(answer)

    st.subheader("Retrieved Context (RAG)")
    st.write(context)