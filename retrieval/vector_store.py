from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import SentenceTransformerEmbeddings

def create_vector_store(chunks):
    texts = [chunk["content"] for chunk in chunks]
    metadatas = [{"source": chunk["source"]} for chunk in chunks]

    embeddings = SentenceTransformerEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vector_store = FAISS.from_texts(
        texts=texts,
        embedding=embeddings,
        metadatas=metadatas
    )

    return vector_store
