from langchain_huggingface import HuggingFaceEndpoint

def get_llm():
    """
    Qwen2.5-7B-Instruct via Hugging Face Inference (FREE tier, less crowded)
    """
    return HuggingFaceEndpoint(
        repo_id="Qwen/Qwen2.5-7B-Instruct",
        temperature=0.2,
        max_new_tokens=400,
        top_p=0.9,
        repetition_penalty=1.05
    )
