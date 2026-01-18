from langchain_core.prompts import ChatPromptTemplate

def get_rag_prompt():
    return ChatPromptTemplate.from_template(
        """
You are a knowledgeable tutor.

Answer the question ONLY using the context provided below.
If the answer is not present in the context, say exactly:
"I don't know based on the provided document."

Context:
{context}

Question:
{question}

Answer clearly, accurately, and like a tutor.
"""
    )
