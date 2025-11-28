import os
import shutil
import tempfile
from dotenv import load_dotenv
from fastapi import UploadFile
from logger import logger
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()
UPLOAD_DIR = os.getenv("UPLOAD_DIR", "./uploaded_pdfs")

# Save Uploaded PDF Files to folder
def save_uploaded_files(files:list[UploadFile]) -> list[str]:

    # Create the upload directory
    os.makedirs(UPLOAD_DIR, exist_ok = True)
    file_paths = []

    # Save each file to directory
    for file in files:
        filename = os.path.basename(file.filename)
        temp_path = os.path.join(UPLOAD_DIR, filename)

        try:
            with open(temp_path, "wb") as f:
                shutil.copyfileobj(file.file, f)
            file_paths.append(temp_path)
        except Exception as e:
            logger.exception(f"Error uploading pdf: {str(e)}")

    return file_paths # Return list of file paths

# Load Documents to Extract text from PDFs
def load_documents(file_paths: list[str]) -> list:
    docs = []
    for path in file_paths:
        loader = PyPDFLoader(path)
        docs.extend(loader.load())

    return docs # Return text of the PDF

# Split Documents into multiple chunks
def split_documents(docs: list) -> list:
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = splitter.split_documents(docs)
    return texts