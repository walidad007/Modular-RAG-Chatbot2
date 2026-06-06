import streamlit as st

from components.upload_ui import render_upload_section
from components.chat_ui import render_chat_section

st.set_page_config(page_title="RAG Chatbot")

st.title("AI RAG Chatbot")

render_upload_section()

render_chat_section()
