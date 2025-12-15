import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
# from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain.chains.retrieval import create_retrieval_chain

# Load Environment Variable
load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

def get_llm_chain(vectorstore):
    api_key = GROQ_API_KEY
    llm = ChatGroq(
        model_name = "qwen/qwen3-32b"        
    )
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    # return RetrievalQA.from_chain_type(
    #     llm=llm,
    #     chain_type = "stuff",
    #     retriever = retriever,
    #     return_source_documents = True
    # )
    return create_retrieval_chain(
        retriever=retriever,
        llm=llm,
        return_source_documents=True
    )