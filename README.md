📘 RAG Tutor – Chunking, Retrieval & Tutor (Streamlit)
======================================================

A **Retrieval-Augmented Generation (RAG) Tutor** that allows users to upload PDF documents and ask questions grounded strictly in the document content.The system uses **semantic search + LLM reasoning** to behave like a tutor rather than a chatbot.

🚀 Project Overview
-------------------

Traditional LLMs hallucinate because they rely only on pre-trained knowledge.This project solves that by implementing a **RAG pipeline** where:

1.  Documents are **chunked**
    
2.  Converted into **vector embeddings**
    
3.  Stored in a **FAISS vector database**
    
4.  Relevant context is retrieved for each query
    
5.  An LLM generates **grounded, tutor-style answers**
    

If the answer is **not present in the document**, the model explicitly says so.

🧠 Key Features
---------------

*   📄 Upload any PDF document
    
*   ✂️ Automatic text chunking with metadata
    
*   🔎 Semantic similarity search using FAISS
    
*   🧠 Tutor-style answers (not raw chunk dumps)
    
*   🚫 Hallucination control via strict prompting
    
*   ⏳ Rate-limit aware (Hugging Face free tier safe)
    
*   🔁 Clear vectorstore & upload new documents
    
*   ☁️ Ready for Streamlit Community Cloud deployment
    

🏗️ Architecture (High Level)
-----------------------------

```
PDF Upload
   ↓
PDF Loader
   ↓
Text Chunking
   ↓
Embedding Model
   ↓
FAISS Vector Store
   ↓
Similarity Search (Top-K Chunks)
   ↓
Prompt + Context
   ↓
LLM (Qwen / Mixtral via HF)
   ↓
Tutor-Style Answer

```

🛠️ Tech Stack
--------------

### Frontend

*   **Streamlit** – UI and interaction layer
    

### Backend / ML

*   **LangChain (v1)** – RAG orchestration
    
*   **FAISS** – Vector similarity search
    
*   **Sentence Transformers** – Embeddings
    
*   **Hugging Face Inference API** – Free LLM inference
    
*   **Qwen2.5 / Mixtral** – Instruction-tuned LLMs
    

### Utilities

*   **Python**
    
*   **dotenv** – Environment variable handling
    

📂 Project Structure
--------------------
```
rag-tutor-streamlit/
│
├── app.py                     # Main Streamlit app
├── requirements.txt           # Project dependencies
├── README.md                  # Documentation
├── .gitignore                 # Ignored files
│
├── rag/
│   ├── loader.py              # PDF loading logic
│   ├── splitter.py            # Chunking strategy
│   ├── embeddings.py          # Embedding model
│   ├── vectorstore.py         # FAISS vector store
│   ├── llm.py                 # Hugging Face LLM setup
│   ├── prompt.py              # Strict RAG prompt
│   ├── chain.py               # Context formatting
│   └── utils.py               # Helper utilities
│
└── data/                      # Uploaded PDFs (runtime)

```


🧠 RAG Prompt Strategy (Hallucination Control)
----------------------------------------------

The model is instructed to:

*   Answer **only using retrieved context**
    
*   _"I don't know based on the provided document"_if the answer is not found
    

This ensures:

*   No fabricated answers
    
*   High factual accuracy
    
*   Trustworthy responses
    

⏳ Rate Limiting & Reliability
-----------------------------

Because the project uses **Hugging Face Free Tier**, the following safeguards are implemented:

*   UI-level throttling (1 request per 5 seconds)
    
*   Token limits (max\_new\_tokens)
    
*   Graceful fallback when the model is busy
    
*   Retrieval results shown even if LLM is unavailable
    

This makes the system **robust and production-aware**.

🔐 Environment Variables
------------------------

The project requires a Hugging Face API token.

Create a .env file locally:

`   HUGGINGFACEHUB_API_TOKEN=your_token_here   `

> ⚠️ .env is excluded via .gitignore and never committed.

▶️ Running the Project Locally
------------------------------

### 1️⃣ Create virtual environment
```
python -m venv venv  source venv/bin/activate  
# Windows: venv\Scripts\activate   
```

### 2️⃣ Install dependencies

`   pip install -r requirements.txt   `

### 3️⃣ Run Streamlit app

`   streamlit run app.py   `

🧪 Example Use Case
-------------------

1.  Upload a dictionary / textbook / notes PDF
    
2.  Define apple in this document
    
3.  The tutor:
    
    *   Retrieves relevant chunks
        
    *   Generates a grounded explanation
        
    *   Avoids hallucinations
        

📈 Why This Project Matters
---------------------------

This project demonstrates:

*   Real-world **RAG architecture**
    
*   Modern **LangChain v1** usage
    
*   Vector database lifecycle management
    
*   LLM rate-limit handling
    
*   Clean Streamlit engineering
    
*   Production-aware ML system design
    

🧠 Interview-Ready Talking Points
---------------------------------

*   “I separated retrieval from generation to prevent hallucination.”
    
*   “Vector stores are treated as runtime databases, not version-controlled artifacts.”
    
*   “I implemented UI-level throttling to handle LLM rate limits gracefully.”
    
*   “The system remains useful even when the LLM is unavailable.”
    

🚀 Future Improvements
----------------------

*   Multi-PDF support
    
*   Chat history memory
    
*   Source citation per answer
    
*   Async retrieval
    
*   Alternative vector stores (Chroma / Milvus)
    
*   Deployment on Streamlit Community Cloud
    

📜 License
----------

This project is licensed under the **Apache 2.0 License**.

🙌 Author
---------

**Maddikatla Chaitanya**B.E Undergraduate | Full-Stack & ML Enthusiast
