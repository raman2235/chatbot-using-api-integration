import streamlit as st
from chatbot_engine import get_answer

st.set_page_config(page_title="Gemini RAG Chatbot")
st.title("🤖 Chatbot using Gemini + LangChain")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

query = st.chat_input("Ask something...")
if query:
    st.chat_message("user").write(query)
    st.session_state.messages.append({"role": "user", "content": query})

    with st.spinner("Gemini is thinking..."):
        reply = get_answer(query)
    st.chat_message("assistant").write(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})