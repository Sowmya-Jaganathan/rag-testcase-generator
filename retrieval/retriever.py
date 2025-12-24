def retrieve_chunks(vector_store, query, top_k=3):
    results = vector_store.similarity_search(query, k=top_k)
    return results
