from server.rag.rag_chain import build_rag_chain
from server.rag.retriever import get_retriever


def ask_question(query):
    """
    Ask a question from the RAG chatbot.
    Retrieves relevant document chunks from the vector store
    and generates an answer using the LLM.
    """

    # Step 1: Create a fresh retriever instance so it reflects
    # the latest state of the vector store after PDF upload
    retriever = get_retriever()

    # Step 2: Search the vector store for chunks relevant to the query
    retrieved_docs = retriever.invoke(query)

    # Step 3: Print debug info to terminal to verify retrieval is working
    print("\n\n========== RETRIEVED DOCS ==========\n")
    print(f"Retrieved Chunks: {len(retrieved_docs)}")

    # Step 4: If no relevant chunks found, return early with a clear message
    # This prevents the LLM from giving a generic hallucinated answer
    if not retrieved_docs:
        return {
            "answer": "I could not find relevant information in the uploaded documents. Please make sure you have uploaded a PDF and try again.",
            "sources": [],
        }

    # Step 5: Print each retrieved chunk to terminal for debugging
    for doc in retrieved_docs:
        print(doc.page_content[:500])
        print("\n------------------\n")

    # Step 6: Build a fresh RAG chain on every call
    # Previously this was created once at module level (outside the function),
    # which meant it used an empty vector store from server startup time.
    # Now it is created here so it always picks up the latest uploaded documents.
    qa_chain = build_rag_chain()

    # Step 7: Run the query through the RAG chain (retriever + LLM combined)
    result = qa_chain.invoke({"query": query})

    # Step 8: Extract source metadata (page number, filename) from retrieved docs
    sources = []
    for doc in result["source_documents"]:
        page = doc.metadata.get("page", "Unknown")
        sources.append(
            {
                # Page numbers in PDF are 0-indexed, so add 1 for display
                "page": page + 1 if isinstance(page, int) else page,
                "source": doc.metadata.get("source", ""),
            }
        )

    # Step 9: Return the final answer and source references
    return {"answer": result["result"], "sources": sources}
