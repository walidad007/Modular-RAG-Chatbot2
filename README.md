# DocuMind — AI-Powered Document Intelligence Chatbot

> Upload any PDF. Ask anything. Get precise, source-backed answers — instantly.

DocuMind is a production-oriented AI chatbot that lets users have natural conversations with their PDF documents. Instead of manually searching through reports, contracts, or manuals, users simply ask questions and receive accurate answers grounded directly in their uploaded content.

---

## Features

- **PDF Upload & Auto-Processing** — Upload one or more PDF files; the system handles text extraction, chunking, and indexing automatically
- **Semantic Search** — Finds the most relevant document sections using vector embeddings, not just keyword matching
- **Source-Cited Answers** — Every response includes the exact page number and document it was pulled from
- **Hallucination Prevention** — The LLM only answers from uploaded content; it will not fabricate information
- **Knowledge Base Management** — Clear and replace documents at any time to start fresh
- **Chat History** — Full conversation history maintained within each session
- **Modular Architecture** — Each component (loader, embedder, retriever, LLM) is independently swappable
- **REST API Backend** — FastAPI backend exposes clean endpoints, ready for integration into any existing system

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | FastAPI + Uvicorn |
| LLM | Groq API (LLaMA 3.3 70B) |
| Embeddings | HuggingFace `all-MiniLM-L6-v2` |
| Vector Database | ChromaDB |
| RAG Framework | LangChain |
| PDF Processing | PyPDF |
| Language | Python 3.11 |

---

## Installation

### Prerequisites

- Python 3.11
- [uv](https://docs.astral.sh/uv/getting-started/installation/) — modern Python package manager

Install uv if you don't have it:

```bash
# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/documind.git
cd documind
```

### 2. Install Dependencies

```bash
uv sync
```

That's it. `uv sync` reads `pyproject.toml` and `uv.lock` together — creates a virtual environment automatically and installs all dependencies at exact pinned versions.

### 3. Configure Environment Variables

Create a `.env` file inside the `server/` directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get your free Groq API key at [console.groq.com](https://console.groq.com)

> **Prefer pip?** Run `uv export --format requirements-txt > requirements.txt` to generate
> a standard requirements file, then `pip install -r requirements.txt`.
---

## Usage

### Start the Backend Server

```bash
uvicorn server.main:app --reload
```

The API will be available at `http://localhost:8000`

### Start the Frontend

Open a second terminal:

```bash
cd client
streamlit run app.py
```

The UI will open at `http://localhost:8501`

### Workflow

1. Open the Streamlit interface
2. Upload one or more PDF files using the sidebar
3. Wait for the processing confirmation
4. Type your question in the chat input
5. Receive an answer with source page references

---

## Project Structure

```
documind/
│
├── client/                        # Streamlit frontend
│   ├── app.py                     # Main Streamlit entry point
│   ├── components/
│   │   ├── upload_ui.py           # PDF upload interface
│   │   ├── chat_ui.py             # Chat interface
│   │   └── history_ui.py          # Conversation history display
│   └── services/
│       └── api.py                 # HTTP client for backend communication
│
├── server/                        # FastAPI backend
│   ├── main.py                    # API routes: /upload, /chat, /clear-kb
│   ├── config.py                  # Environment variables and constants
│   ├── logger.py                  # Structured logging
│   └── rag/                       # Core RAG pipeline (modular)
│       ├── pdf_loader.py          # PDF ingestion and storage
│       ├── text_splitter.py       # Document chunking logic
│       ├── embeddings.py          # Embedding model loader
│       ├── vectorstore.py         # ChromaDB create / load / clear
│       ├── retriever.py           # Semantic retriever configuration
│       ├── rag_chain.py           # LangChain RetrievalQA chain builder
│       └── chat_service.py        # Orchestrates retrieval + LLM response
│
├── server/storage/
│   ├── uploaded_pdfs/             # Stores user-uploaded PDF files
│   └── chroma_db/                 # Persisted vector embeddings
│
└── pyproject.toml                 # Project metadata and dependencies
```

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Health check |
| `POST` | `/upload` | Upload and process PDF files |
| `POST` | `/chat?query=...` | Ask a question against the knowledge base |
| `POST` | `/clear-kb` | Clear all uploaded documents and embeddings |

---

## Roadmap

- [ ] Multi-collection support (separate knowledge bases per project)
- [ ] Hybrid search (vector + BM25 keyword)
- [ ] Conversation memory across sessions
- [ ] Support for pdfs, Word (.docx) and plain text files
- [ ] User authentication
- [ ] Cloud deployment (Railway / Render / AWS)
- [ ] Citation highlighting in source documents

---

## Author

**Wali Dad**

AI Chatbot Developer specializing in RAG pipelines, LangChain, and document intelligence systems built with Python.

- GitHub: [https://github.com/walidad007](https://github.com/walidad007)
- Upwork: [https://www.upwork.com/freelancers/~0144c1feb305f1ff11](https://www.upwork.com/freelancers/~0144c1feb305f1ff11)