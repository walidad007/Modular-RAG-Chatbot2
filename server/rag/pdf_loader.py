import os
from langchain_community.document_loaders import PyPDFLoader

# Calculate absolute path from this file's location
# __file__ = server/rag/pdf_loader.py
# Go up 2 levels to reach: server/
# Then: server/storage/uploaded_pdfs
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "storage", "uploaded_pdfs")

# Create folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Print path at startup so you can verify in terminal
print(f"\n===== PDF LOADER INIT =====")
print(f"UPLOAD_FOLDER resolved to: {UPLOAD_FOLDER}")
print(f"Folder exists: {os.path.exists(UPLOAD_FOLDER)}")


async def save_uploaded_pdfs(files):
    """Save uploaded PDF files to disk."""

    for file in files:

        file_path = os.path.join(UPLOAD_FOLDER, file.filename)

        print(f"\n[SAVE] Saving file: {file.filename}")
        print(f"[SAVE] Full path: {file_path}")

        content = await file.read()

        # Safety check: make sure file has content
        if not content:
            print(f"[ERROR] File is empty: {file.filename}")
            continue

        with open(file_path, "wb") as f:
            f.write(content)

        # Verify file actually saved on disk
        if os.path.exists(file_path):
            print(
                f"[SAVE] SUCCESS — {file.filename} ({os.path.getsize(file_path)} bytes)"
            )
        else:
            print(f"[ERROR] File NOT found after saving: {file_path}")

    return "PDFs uploaded successfully"


def load_pdfs():
    """Load all PDF files from upload folder and return documents."""

    documents = []

    print("\n===== PDF LOADER =====")
    print(f"Reading from: {UPLOAD_FOLDER}")
    print(f"Files found: {os.listdir(UPLOAD_FOLDER)}")

    for filename in os.listdir(UPLOAD_FOLDER):

        if filename.endswith(".pdf"):

            path = os.path.join(UPLOAD_FOLDER, filename)

            print(f"[LOAD] Loading: {path}")

            loader = PyPDFLoader(path)
            docs = loader.load()

            print(f"[LOAD] Pages loaded: {len(docs)}")

            documents.extend(docs)

    print(f"[LOAD] Total documents loaded: {len(documents)}")

    return documents
