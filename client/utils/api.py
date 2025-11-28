import requests
from config import API_URL

def upload_pdfs_api(files):
    # Preparing PDF Files for upload via HTTP Request
    files_payload = [("files", (f.name, f.read(), "application/pdf")) for f in files]
    return requests.post(f"{API_URL}/upload-pdfs", files=files_payload) # Send HTTP Post 

def ask_question_api(question):
    return requests.post(f"{API_URL}/ask", data={"question": question})