from server.rag.vectorstore import load_vectorstore


def get_retriever():
    """
    Create retriever.
    """

    vectorstore = load_vectorstore()

    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    return retriever
