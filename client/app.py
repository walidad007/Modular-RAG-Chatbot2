import streamlit as st

from components.upload_ui import render_upload_section
from components.chat_ui import render_chat_section

st.set_page_config(page_title="Modular RAG Chatbot", layout="wide")

with st.sidebar:

    st.title("📚 Knowledge Base")

    render_upload_section()

st.title("🤖 RAG Chatbot")

render_chat_section()
