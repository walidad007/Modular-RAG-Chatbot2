from fastapi import FastAPI, UploadFile, File
from server.rag.chat_service import ask_question
from server.rag.pdf_loader import save_uploaded_pdfs, load_pdfs, clear_uploaded_pdfs
from server.rag.text_splitter import split_documents
from server.rag.vectorstore import (
    create_vectorstore,
    clear_vectorstore,
)
from typing import List

app = FastAPI()

print("\n🔥🔥🔥 MY MAIN.PY LOADED 🔥🔥🔥\n")


@app.get("/")
def home():
    return {"message": "RAG Chatbot API Running"}


@app.post("/upload")
async def upload_pdfs(files: List[UploadFile] = File(...)):

    print("\n🔥 UPLOAD ENDPOINT HIT 🔥")

    print("FILES RECEIVED:", len(files))

    for f in files:
        print("FILE:", f.filename)

    await save_uploaded_pdfs(files)

    documents = load_pdfs()

    print(f"Documents Loaded: {len(documents)}")

    chunks = split_documents(documents)

    print(f"Chunks Created: {len(chunks)}")

    vectorstore = create_vectorstore(chunks)

    print("Documents stored:", vectorstore._collection.count())

    return {
        "status": "success",
        "message": "PDF processed successfully",
    }


# ==========================================================
# Clear Knowledge Base
#
# Removes:
# 1. All uploaded PDFs
# 2. All vector embeddings
#
# Allows user to start with a fresh dataset
# ==========================================================


@app.post("/clear-kb")
def clear_kb():

    clear_uploaded_pdfs()

    clear_vectorstore()

    return {"status": "success", "message": "Knowledge Base cleared successfully"}


@app.post("/chat")
def chat(query: str):

    result = ask_question(query)

    if result is None:
        return {
            "query": query,
            "answer": "No relevant information found.",
            "sources": [],
        }

    return {"query": query, "answer": result["answer"], "sources": result["sources"]}
