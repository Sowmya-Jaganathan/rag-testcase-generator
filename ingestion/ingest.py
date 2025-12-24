from ingestion.text_loader import load_text_files

def ingest_all(data_folder="data/sample_docs"):
    documents = []
    documents.extend(load_text_files(data_folder))
    return documents
