import os
from dotenv import load_dotenv

# from langchain.chains.retrieval_qa.base import RetrievalQA

from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq

# from langchain.prompts import PromptTemplate
from server.rag.retriever import get_retriever

load_dotenv()


def build_rag_chain():
    """
    Build RAG chain.
    """

    llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model="llama-3.3-70b-versatile")

    retriever = get_retriever()

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm, retriever=retriever, return_source_documents=True
    )

    return qa_chain
