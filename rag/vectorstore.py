import os
from langchain_community.vectorstores import FAISS

def create_or_load_vectorstore(chunks, embedding_model):
    """
    Creates or loads FAISS vector store
    """
    if os.path.exists("vectorstore"):
        return FAISS.load_local(
            "vectorstore",
            embedding_model,
            allow_dangerous_deserialization=True
        )

    vectorstore = FAISS.from_documents(chunks, embedding_model)
    vectorstore.save_local("vectorstore")
    return vectorstore
