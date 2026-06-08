import streamlit as st

from services.api import send_query


def render_chat_section():

    query = st.text_input(
        "Ask a question"
    )

    if st.button("Send"):

        if not query.strip():

            st.warning(
                "Please enter a question."
            )
            return

        with st.spinner(
            "Searching knowledge base..."
        ):

            response = send_query(query)

        answer = response.get("answer")

        if answer:

            st.subheader("Answer")
            st.write(answer)

        sources = response.get("sources", [])

        if sources:

            st.subheader("Sources")

            for source in sources:

                st.write(
                    f"Page {source['page']} | "
                    f"{source['source']}"
                )