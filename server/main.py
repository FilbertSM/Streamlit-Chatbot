from typing import List
from fastapi import FastAPI, UploadFile, File, Form, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from logger import logger
from modules.pdf_handlers import save_uploaded_files, load_documents, split_documents
from modules.store_vectors import store_vectors, load_vectors, get_retriever
from modules.query_chain import query_chain
from langchain_ollama.llms import OllamaLLM

app = FastAPI(title="GAIA")

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"]
)

# Error Handling Middleware
@app.middleware("http")
async def catch_exception_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
         logger.exception("UNHANDLED EXCEPTION")
         return JSONResponse(status_code=500, content={"error": str(e)})
    
# Upload PDF
@app.post("/upload-pdfs")
async def upload_pdfs(files: List[UploadFile] = File(...)):
    try:
        logger.info(f"Received {len(files)} files")

        # Save Files
        file_paths = save_uploaded_files(files)
        logger.info("Documents Saved")

        # Load Files
        docs = load_documents(file_paths)
        logger.info("Documents Loaded")

        # Split Files
        chunks = split_documents(docs)
        logger.info("Documents Split")

        # Store Vectors
        store_vectors(chunks)
        logger.info("Vectors Stored")

        return {"message": "File processed and Vector stored"}
    except Exception as e:
        logger.exception("Error during PDF upload")
        return JSONResponse(status_code=500, content={"error": str(e)})
    
# Handle Queries
@app.post("/ask")
async def ask_question(question: str = Form(...)):
    try:
        logger.info(f"User Query: {question}")

        # Prepare LLM
        llm = OllamaLLM(model="qwen3-vl:235b-cloud", base_url="http://localhost:11434")

        # Prepare Retriever
        vectorstore = load_vectors()
        retriever = get_retriever(vectorstore)

        # Chain Query
        result = query_chain(retriever, llm, question)
        logger.info("Query Successful")
        
        return result
    except Exception as e:
        logger.exception("Error during processing question")
        return JSONResponse(status_code=500, content={"error": str(e)})