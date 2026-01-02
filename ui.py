import streamlit as st
import json

from ingestion.ingest import ingest_documents
from retrieval.chunker import chunk_documents
from retrieval.vector_store import create_vector_store
from retrieval.retriever import retrieve_chunks
from generation.generator import generate_test_cases
from guards.context_guard import has_sufficient_context

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="RAG Test Case Generator",
    layout="centered"
)

st.title("AI Test Case Generator (RAG)")

st.write(
    "This application generates structured test cases from multiple documents "
    "and UI screenshots using a Retrieval-Augmented Generation (RAG) pipeline."
)

# ---------------- Load Pipeline ----------------
@st.cache_resource
def load_pipeline():
    docs = ingest_documents()
    chunks = chunk_documents(docs)
    vector_store = create_vector_store(chunks)
    return vector_store

vector_store = load_pipeline()

# ---------------- User Input ----------------
query = st.text_input(
    "Enter your query",
    placeholder="Create use cases for user signup"
)

# ---------------- Generate Button ----------------
if st.button(" Generate Test Cases"):
    if not query:
        st.warning("Please enter a query first.")
    else:
        retrieved_chunks = retrieve_chunks(vector_store, query)

        # ---------------- Guard Check ----------------
        if not has_sufficient_context(retrieved_chunks):
            st.error("❌ Not enough context to generate test cases.")
        else:
            context = "\n\n".join([chunk.page_content for chunk in retrieved_chunks])

            # ---------------- Generate Output ----------------
            result = generate_test_cases(context, query)

            st.subheader("✅ Generated Test Cases")
            st.json(json.loads(result))

            # ---------------- Retrieved Context (Proof of RAG + OCR) ----------------
            with st.expander("🔍 View Retrieved Context (RAG Evidence)"):
                for i, chunk in enumerate(retrieved_chunks, start=1):
                    source = chunk.metadata.get("source", "unknown")
                    st.markdown(f"**Chunk {i} | Source:** `{source}`")
                    st.code(chunk.page_content[:500])
