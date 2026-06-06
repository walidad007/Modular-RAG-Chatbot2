from fastapi import FastAPI, UploadFile, File
from server.rag.chat_service import ask_question
from server.rag.pdf_loader import save_uploaded_pdfs, load_pdfs
from server.rag.text_splitter import split_documents
from server.rag.vectorstore import create_vectorstore
from typing import List

app = FastAPI()

print("\n🔥🔥🔥 MY MAIN.PY LOADED 🔥🔥🔥\n")


@app.get("/")
def home():
    return {"message": "RAG Chatbot API Running"}


from fastapi import UploadFile, File


@app.post("/test-upload")
async def test_upload(file: UploadFile = File(...)):
    print("TEST FILE:", file.filename)
    return {"filename": file.filename}


@app.post("/test-multi-upload")
async def test_multi_upload(files: List[UploadFile] = File(...)):
    print("FILES RECEIVED:", len(files))

    return {"count": len(files)}


@app.post("/upload")
async def upload_pdfs(file: UploadFile = File(...)):

    print("\n🔥 UPLOAD ENDPOINT HIT 🔥")

    await save_uploaded_pdfs([file])

    documents = load_pdfs()

    print(f"Documents Loaded: {len(documents)}")

    chunks = split_documents(documents)

    print(f"Chunks Created: {len(chunks)}")

    vectorstore = create_vectorstore(chunks)

    print("Documents stored:", vectorstore._collection.count())

    return {
        "status": "success",
        "message": "PDF processed successfully"
    }


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
