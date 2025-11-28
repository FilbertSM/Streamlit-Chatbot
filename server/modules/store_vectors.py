import os
from dotenv import load_dotenv
from pathlib import Path
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Define Folders
load_dotenv()
UPLOAD_DIR = os.getenv("UPLOAD_DIR", "./uploaded_pdfs") # Documents Dir
PERSIST_DIR = os.getenv("PERSIST_DIR", "./chroma_store") # Vector Data Dir
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Embedding Models
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# Store Vectors in Database
def store_vectors(texts: list)-> Chroma:
    
    # If exist Load Vector Store and Add new documents
    if os.path.exists(PERSIST_DIR) and os.listdir(PERSIST_DIR):
        vectorstore = Chroma(persist_directory=PERSIST_DIR, embedding_function=embeddings)
        vectorstore.add_documents(texts)
        vectorstore.persist()
    else: # Else create new Vector Store
        vectorstore = Chroma.from_documents(
            documents = texts,
            embedding = embeddings,
            persist_directory = PERSIST_DIR
        )
        vectorstore.persist()

    return vectorstore

# Load Vectorstore
def load_vectors():
    return Chroma(persist_directory=PERSIST_DIR, embedding_function=embeddings)

# Retrieve Relevant Chunks
def get_retriever(vectorstore, k=3):
    return vectorstore.as_retriever(search_kwargs={"k": k})