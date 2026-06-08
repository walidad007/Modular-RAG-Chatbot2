import streamlit as st
from services.api import upload_pdfs


def render_upload_section():

    st.subheader("Upload PDFs")

    uploaded_files = st.file_uploader(
        "Choose PDFs", type=["pdf"], accept_multiple_files=True
    )

    if uploaded_files:

        if st.button("Upload PDFs"):

            files = []

            for pdf in uploaded_files:

                files.append(("files", (pdf.name, pdf.getvalue(), "application/pdf")))

            response = upload_pdfs(files)

            st.write("DEBUG RESPONSE")
            st.json(response)

            if "message" in response:
                st.success(response["message"])
