from pathlib import Path

def load_text_files(folder_path):
    documents = []

    for file_path in Path(folder_path).glob("*.txt"):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

            documents.append({
                "content": content,
                "source": file_path.name
            })

    return documents
