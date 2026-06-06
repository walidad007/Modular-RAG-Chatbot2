import streamlit as st

from services.api import send_query


def render_chat_section():
    """
    Render chatbot UI.
    """

    query = st.text_input("Ask question")

    if st.button("Send"):

        if not query.strip():
            st.warning("Please enter a question.")
            return

        with st.spinner("Searching documents..."):
            response = send_query(query)

        st.write("### Debug Response")
        st.json(response)

        answer = response.get("answer")

        if answer:

            st.write("### Answer")
            st.write(answer)

        else:

            st.error("No answer returned from backend.")

        sources = response.get("sources", [])

        if sources:

            st.write("### Sources")

            for source in sources:

                st.write(f"Page {source.get('page')} | " f"{source.get('source')}")
