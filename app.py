import os
import time
import streamlit as st
from dotenv import load_dotenv

from rag.loader import load_pdf
from rag.splitter import split_documents
from rag.embeddings import get_embedding_model
from rag.vectorstore import create_or_load_vectorstore
from rag.utils import clear_vectorstore

# 🔥 RAG + LLM imports
from rag.llm import get_llm
from rag.prompt import get_rag_prompt
from rag.chain import format_docs

# -------------------- Load Environment --------------------
load_dotenv()  # loads HUGGINGFACEHUB_API_TOKEN

# -------------------- Streamlit Config --------------------
st.set_page_config(
    page_title="RAG Tutor",
    layout="wide"
)

st.title("📘 RAG Tutor – Chunking, Retrieval & Tutor")

# -------------------- Sidebar Controls --------------------
st.sidebar.header("⚙️ Settings")

if st.sidebar.button("🗑️ Clear Vectorstore"):
    clear_vectorstore()

    for key in ["vectorstore", "uploaded_file_name", "chunks", "last_llm_call"]:
        if key in st.session_state:
            del st.session_state[key]

    st.sidebar.success("Vectorstore cleared. Upload a new PDF.")

# -------------------- PDF Upload --------------------
uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file:
    # Process only if new file is uploaded
    if st.session_state.get("uploaded_file_name") != uploaded_file.name:
        st.session_state.uploaded_file_name = uploaded_file.name

        os.makedirs("data", exist_ok=True)
        file_path = os.path.join("data", uploaded_file.name)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # -------------------- Load & Chunk --------------------
        documents = load_pdf(file_path)
        chunks = split_documents(documents)

        # ✅ STORE CHUNKS SAFELY
        st.session_state["chunks"] = chunks

        st.success(f"PDF loaded and split into {len(chunks)} chunks")

        # -------------------- Embeddings + Vectorstore --------------------
        embeddings = get_embedding_model()
        vectorstore = create_or_load_vectorstore(chunks, embeddings)
        st.session_state["vectorstore"] = vectorstore

    else:
        vectorstore = st.session_state.get("vectorstore")

    # -------------------- Sample Chunk Display --------------------
    sample_chunks = st.session_state.get("chunks")

    if vectorstore and sample_chunks:
        st.subheader("🔍 Sample Chunk")
        st.write(sample_chunks[0].page_content)
        st.caption(f"Metadata: {sample_chunks[0].metadata}")

        # -------------------- RAG Tutor --------------------
        st.divider()
        st.subheader("🧠 Ask the Tutor")

        question = st.text_input("Ask a question from the document")

        if question:
            # -------- Simple rate limiting (HF free tier protection) --------
            now = time.time()
            last_call = st.session_state.get("last_llm_call", 0)

            if now - last_call < 5:
                st.warning("⏳ Please wait a few seconds before asking another question.")
                st.stop()

            st.session_state["last_llm_call"] = now

            docs = st.session_state["vectorstore"].similarity_search(
                question,
                k=4
            )

            context = format_docs(docs)

            llm = get_llm()
            prompt = get_rag_prompt()
            chain = prompt | llm

            try:
                response = chain.invoke({
                    "context": context,
                    "question": question
                })

                st.subheader("📘 Tutor Answer")
                st.write(response if isinstance(response, str) else response.content)

            except Exception:
                st.error("⚠️ Model is busy or rate-limited. Please try again in a few seconds.")

            with st.expander("🔍 Retrieved Context"):
                for i, doc in enumerate(docs, start=1):
                    st.markdown(f"**Chunk {i}**")
                    st.write(doc.page_content)
                    st.caption(doc.metadata)
