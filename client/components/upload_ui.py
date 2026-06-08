import streamlit as st

from services.api import (
    upload_pdfs,
    clear_kb,
)


def render_upload_section():
    """
    Render PDF upload and Knowledge Base controls.
    """

    st.subheader("📚 Knowledge Base")

    # ==========================================================
    # Clear Knowledge Base Button
    #
    # Deletes:
    # - All uploaded PDF files
    # - All ChromaDB vectors/embeddings
    #
    # This allows the user to start with a fresh dataset.
    # ==========================================================

    if st.button("🗑 Clear Knowledge Base"):

        with st.spinner("Clearing Knowledge Base..."):

            response = clear_kb()

        st.success(
            response.get(
                "message",
                "Knowledge Base cleared successfully.",
            )
        )

        st.rerun()

    # ==========================================================
    # PDF Upload Section
    #
    # Allows uploading one or more PDFs which will be:
    # 1. Saved to disk
    # 2. Loaded and split into chunks
    # 3. Embedded
    # 4. Stored in ChromaDB
    # ==========================================================

    uploaded_files = st.file_uploader(
        "Choose PDFs",
        type=["pdf"],
        accept_multiple_files=True,
    )

    if uploaded_files:

        st.success(f"{len(uploaded_files)} PDF(s) selected")

        if st.button("Build Knowledge Base"):

            with st.spinner("Creating embeddings and vector database..."):

                files = []

                for pdf in uploaded_files:

                    files.append(
                        (
                            "files",
                            (
                                pdf.name,
                                pdf.getvalue(),
                                "application/pdf",
                            ),
                        )
                    )

                response = upload_pdfs(files)

            if "message" in response:

                st.success(response["message"])
                st.toast("Knowledge Base Ready!", icon="✅")

            else:

                st.error("Failed to build Knowledge Base.")
