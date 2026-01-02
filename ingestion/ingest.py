import os
from ingestion.text_loader import load_text_file
from ingestion.image_loader import load_image_text

def ingest_documents(data_dir="data/sample_docs"):
    documents = []

    for root, _, files in os.walk(data_dir):
        for file in files:
            file_path = os.path.join(root, file)

            if file.endswith(".txt"):
                content = load_text_file(file_path)

            elif file.lower().endswith((".png", ".jpg", ".jpeg")):
                content = load_image_text(file_path)

            else:
                continue

            if content and content.strip():
                documents.append({
                    "content": content,
                    "source": file
                })

    return documents
