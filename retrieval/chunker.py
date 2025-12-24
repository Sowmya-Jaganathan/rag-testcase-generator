from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=100
    )

    chunks = []

    for doc in documents:
        split_texts = splitter.split_text(doc["content"])

        for text in split_texts:
            chunks.append({
                "content": text,
                "source": doc["source"]
            })

    return chunks
