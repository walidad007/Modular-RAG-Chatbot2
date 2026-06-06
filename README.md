# Modular RAG Chatbot

A production-oriented Retrieval-Augmented Generation (RAG) chatbot that allows users to upload PDF documents and chat with their content using AI.

## Overview

This project combines document processing, vector search, and Large Language Models (LLMs) to provide accurate answers grounded in uploaded documents.

Instead of relying solely on an LLM's pre-trained knowledge, the chatbot retrieves relevant information from user-uploaded PDFs and uses that context to generate responses.

## Features

* PDF document upload
* Automatic document chunking
* Embedding generation
* ChromaDB vector storage
* Semantic document retrieval
* Context-aware AI responses
* Source-based answer generation
* Modular and scalable architecture
* FastAPI backend
* Streamlit frontend

## Architecture

```text
User
 │
 ▼
Streamlit Frontend
 │
 ▼
FastAPI Backend
 │
 ▼
PDF Processing
 │
 ▼
Text Chunking
 │
 ▼
Embeddings Generation
 │
 ▼
ChromaDB Vector Store
 │
 ▼
Retriever
 │
 ▼
RAG Chain
 │
 ▼
LLM Response
 │
 ▼
Answer Returned to User
```

## Project Structure

```text
modular-rag-chatbot/
│
├── client/
│   ├── app.py
│   └── components/
│       ├── upload_ui.py
│       └── chat_ui.py
│
├── server/
│   ├── main.py
│   ├── storage/
│   │   └── uploaded_pdfs/
│   │
│   └── rag/
│       ├── chat_service.py
│       ├── rag_chain.py
│       ├── retriever.py
│       ├── vectorstore.py
│       └── embeddings.py
│
└── services/
    └── api.py
```

## How It Works

### 1. Document Upload

Users upload one or more PDF documents through the Streamlit interface.

### 2. Text Extraction & Chunking

The system extracts text from PDFs and splits it into smaller chunks for efficient retrieval.

### 3. Embedding Creation

Each chunk is converted into vector embeddings using an embedding model.

### 4. Vector Storage

Embeddings are stored in ChromaDB, enabling semantic search across documents.

### 5. Retrieval

When a user asks a question, the retriever finds the most relevant document chunks.

### 6. Response Generation

The retrieved context is passed to the LLM, which generates a grounded response based on the uploaded documents.

## Technology Stack

### Frontend

* Streamlit

### Backend

* FastAPI
* Uvicorn

### AI & RAG

* LangChain
* Embedding Models
* Retrieval-Augmented Generation (RAG)

### Vector Database

* ChromaDB

### Document Processing

* PDF Parsing
* Text Chunking

## Use Cases

* Internal Knowledge Bases
* Company Documentation Assistants
* Policy & Compliance Q&A
* Educational Material Chatbots
* Research Paper Assistants
* PDF Question Answering Systems

## Key Benefits

* Reduces hallucinations by grounding answers in documents
* Easy document ingestion workflow
* Modular architecture for future enhancements
* Scalable backend design
* Suitable for business and enterprise document search applications

## Future Enhancements

* Multi-document collections
* Metadata filtering
* Conversation memory
* User authentication
* Cloud deployment
* Citation highlighting
* Hybrid search (vector + keyword)
* Support for additional file formats

## Author

Developed as a modular RAG solution demonstrating modern document intelligence workflows using FastAPI, Streamlit, ChromaDB, and LLM-powered retrieval.
