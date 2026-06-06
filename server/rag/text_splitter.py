from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    """
    Split documents into chunks.
    """

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

    chunks = splitter.split_documents(documents)

    # testing
    print(f"Total chunks: {len(chunks)}")

    if chunks:
        print(chunks[0].page_content)

    return chunks
