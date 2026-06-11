import streamlit as st

from services.api import send_query


def render_chat_section():

    # Initialize chat history in session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Display existing chat history
    for message in st.session_state.chat_history:

        with st.chat_message(message["role"]):

            st.write(message["content"])

            # Show sources only for assistant messages
            if message["role"] == "assistant" and message.get("sources"):

                with st.expander("Sources"):

                    for source in message["sources"]:
                        st.caption(f"Page {source['page']} | {source['source']}")

    # Chat input at the bottom
    query = st.chat_input("Ask a question about your documents...")

    if query:

        # Add user message to history and display it
        st.session_state.chat_history.append({"role": "user", "content": query})

        with st.chat_message("user"):
            st.write(query)

        # Get response from backend
        with st.chat_message("assistant"):

            with st.spinner("Searching knowledge base..."):
                response = send_query(query)

            answer = response.get("answer", "No answer found.")
            sources = response.get("sources", [])

            st.write(answer)

            if sources:
                with st.expander("Sources"):
                    for source in sources:
                        st.caption(f"Page {source['page']} | {source['source']}")

        # Save assistant response to history
        st.session_state.chat_history.append(
            {"role": "assistant", "content": answer, "sources": sources}
        )
