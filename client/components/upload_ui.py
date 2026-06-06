import streamlit as st
from services.api import upload_pdfs

def render_upload_section():

    st.subheader("Upload PDF")

    uploaded_file = st.file_uploader(
        "Choose PDF",
        type=["pdf"]
    )

    if uploaded_file:

        if st.button("Upload PDF"):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    "application/pdf"
                )
            }

            response = upload_pdfs(files)

            st.write("DEBUG RESPONSE")
            st.json(response)

            if "message" in response:
                st.success(response["message"])