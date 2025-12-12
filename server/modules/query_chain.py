from logger import logger
from .fetch_role import fetch_role
from langchain_core.prompts import ChatPromptTemplate

def query_chain(retriever, llm, user_input: str, role_id: str):

    # Fetch Roleplay Prompt
    system_prompt = fetch_role(role_id)

    # Create RAG Chain
    template = """
    {role_instruction}

    Here are your Knowledge Base: {knowledgeBase}

    Here is the question to be answered: {question}
    """

    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | llm

    # Invoke Chain
    try:
        logger.debug(f"Running chain for input: {user_input}")

        # Retrieve relevant context
        knowledgeBase = retriever.invoke(user_input)

        # Run the chain with context and user input
        result = chain.invoke({"role_instruction": system_prompt, "knowledgeBase": knowledgeBase, "question": user_input})
        return result
    except Exception as e:
        logger.exception("Error query the chain")
        raise