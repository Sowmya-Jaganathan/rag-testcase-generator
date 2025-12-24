import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from ingestion.ingest import ingest_all
from retrieval.chunker import chunk_documents
from retrieval.vector_store import create_vector_store
from retrieval.retriever import retrieve_chunks
from generation.generator import generate_test_cases
from guards.context_guard import has_sufficient_context

st.set_page_config(page_title="RAG Test Case Generator")

st.title("📄 AI Test Case Generator (RAG)")
st.write("Upload requirement documents and generate test cases using Retrieval-Augmented Generation.")

# Load and index data (simple demo – file-based)
with st.spinner("Indexing documents..."):
    docs = ingest_all()
    chunks = chunk_documents(docs)
    vector_store = create_vector_store(chunks)

query = st.text_input("Enter your query", "Create use cases for user signup")

if st.button("Generate Test Cases"):
    retrieved_chunks = retrieve_chunks(vector_store, query)

    if not has_sufficient_context(retrieved_chunks):
        st.error("Not enough information to generate test cases.")
    else:
        context = "\n\n".join([c.page_content for c in retrieved_chunks])
        result = generate_test_cases(context, query)

        st.subheader("✅ Generated Test Cases")
        st.code(result, language="json")

        with st.expander("🔍 Retrieved Context (Debug View)"):
            for c in retrieved_chunks:
                st.markdown(f"**Source:** {c.metadata['source']}")
                st.text(c.page_content)
