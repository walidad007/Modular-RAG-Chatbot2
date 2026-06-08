import requests

BASE_URL = "http://127.0.0.1:8000"


def send_query(query):
    """
    Send user query to backend.
    """

    response = requests.post(f"{BASE_URL}/chat", params={"query": query})

    return response.json()


def upload_pdfs(files):
    """
    Upload PDFs to backend.
    """

    response = requests.post(f"{BASE_URL}/upload", files=files)

    return response.json()
