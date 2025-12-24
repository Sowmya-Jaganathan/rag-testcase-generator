def has_sufficient_context(retrieved_chunks, min_chunks=1):
    return len(retrieved_chunks) >= min_chunks
