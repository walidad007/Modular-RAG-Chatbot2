import requests

BASE_URL = "http://127.0.0.1:8000"


def send_query(query):
    """
    Send user query to backend.
    """
    response = requests.post(
        f"{BASE_URL}/chat", # changed from /query to /chat
        params={"query": query}
    )
    return response.json()

def upload_pdfs(files):

    print("UPLOAD REQUEST SENT")

    response = requests.post(
        f"{BASE_URL}/upload",
        files=files
    )

    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text)

    return response.json()