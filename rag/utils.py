import shutil
import os

def clear_vectorstore(path="vectorstore"):
    """
    Deletes the FAISS vectorstore directory
    """
    if os.path.exists(path):
        shutil.rmtree(path)
