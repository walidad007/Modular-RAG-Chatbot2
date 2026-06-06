from langchain_chroma import Chroma
from server.rag.embeddings import get_embedding_model
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "storage", "chroma_db")

COLLECTION_NAME = "rag_collection"


def create_vectorstore(chunks):
    embeddings = get_embedding_model()

    vectorstore = Chroma(
        collection_name=COLLECTION_NAME,
        persist_directory=DB_PATH,
        embedding_function=embeddings,
    )

    # Testing phase
    vectorstore.delete_collection()

    vectorstore = Chroma(
        collection_name=COLLECTION_NAME,
        persist_directory=DB_PATH,
        embedding_function=embeddings,
    )


    vectorstore.add_documents(chunks)

    # print("Chunks stored:", len(chunks))
    # print("DB count:", vectorstore._collection.count())

    # ===============Temporarily==============
    print("\n===== CREATE VECTORSTORE =====")
    print("DB_PATH =", DB_PATH)
    print("COLLECTION =", COLLECTION_NAME)
    print("COUNT =", vectorstore._collection.count())


    return vectorstore


# def load_vectorstore():
#     embeddings = get_embedding_model()

#     vectorstore = Chroma(
#         collection_name=COLLECTION_NAME,
#         persist_directory=DB_PATH,
#         embedding_function=embeddings,
#     )

#     print("\n===== VECTOR DB DEBUG =====")
#     print("DB Path:", DB_PATH)
#     print("Count:", vectorstore._collection.count())

#     return vectorstore


# ===============Temporarily==============

def load_vectorstore():
    embeddings = get_embedding_model()

    print("\n===== LOAD VECTORSTORE =====")
    print("DB_PATH =", DB_PATH)
    print("COLLECTION =", COLLECTION_NAME)

    vectorstore = Chroma(
        collection_name=COLLECTION_NAME,
        persist_directory=DB_PATH,
        embedding_function=embeddings,
    )

    count = vectorstore._collection.count()

    print("COUNT =", count)

    return vectorstore