# ipc_sections_search_tool.py

import os

from dotenv import load_dotenv
from crewai.tools import tool
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


VECTOR_DB = None

"""

This tool allows the Legal Assistant to search through the IPC sections vector database to find 
relevant sections based on a user's query. It uses Chroma for vector storage and
HuggingFaceEmbeddings for generating embeddings of the query and IPC sections.

"""



@tool("IPC Sections Search Tool")
def search_ipc_sections(query: str) -> list[dict]:
    """
    Search IPC vector database for sections relevant to the input query.

    Args:
        query (str): User query in natural language.

    Returns:
        list[dict]: List of matching IPC sections with metadata and content.
    """
    # Load environment variables
    load_dotenv()

    # Resolve vector DB path
    persist_dir = os.getenv("PERSIST_DIRECTORY_PATH")
    if not persist_dir:
        raise EnvironmentError("❌ 'PERSIST_DIRECTORY_PATH' is not set in .env")

    persist_dir_path = os.getenv("PERSIST_DIRECTORY_PATH")
    collection_name = os.getenv("IPC_COLLECTION_NAME")

    embedding_function = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Load vectorstore
    

    def get_vectordb():
        global VECTOR_DB

        if VECTOR_DB is None:
            VECTOR_DB = Chroma(
                collection_name=collection_name,
                persist_directory=persist_dir_path,
                embedding_function=embedding_function
            )

        return VECTOR_DB
    
    vector_db = get_vectordb()

    top_k = 3 # can be passed as an argument for flexibility

    # Perform similarity search
    docs = vector_db.similarity_search(query, k=top_k)

    # Format results
    return [
        {
            "section": doc.metadata.get("section"),
            "section_title": doc.metadata.get("section_title"),
            "chapter": doc.metadata.get("chapter"),
            "chapter_title": doc.metadata.get("chapter_title"),
            "content": doc.page_content
        }
        for doc in docs
    ]


# Example usage of the IPC Section Search Tool - uncomment for testing the tool functionality
# query = "What is the IPC section for Theft?"
# results = search_ipc_sections.func(query)
# for r in results:
#     print(r)

# NOTE: Retrieval is a bit slower. Can be improved by caching the vectordb and using GPU for embedding.

