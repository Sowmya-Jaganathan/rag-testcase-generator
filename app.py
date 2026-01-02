from dotenv import load_dotenv
load_dotenv()

from ingestion.ingest import ingest_documents
from retrieval.chunker import chunk_documents
from retrieval.vector_store import create_vector_store
from retrieval.retriever import retrieve_chunks
from generation.generator import generate_test_cases
from guards.context_guard import has_sufficient_context

# Ingest and index documents (TEXT + IMAGE OCR)
docs = ingest_documents()

chunks = chunk_documents(docs)
vector_store = create_vector_store(chunks)

# User query
query = input("Enter your query: ")

# Retrieve relevant chunks
retrieved_chunks = retrieve_chunks(vector_store, query)

if not has_sufficient_context(retrieved_chunks):
    print("❌ Not enough information to generate test cases.")
else:
    context = "\n\n".join(
        [chunk.page_content for chunk in retrieved_chunks]
    )

    result = generate_test_cases(context, query)
    print("\nGenerated Test Cases:\n")
    print(result)
