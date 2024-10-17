from langchain_core.documents import Document


# 
def extract_text_from_txt(file_path: str) -> str:
    with open(file_path, "rb") as f:
        text = f.read().decode("utf-8")
    return text


# 
def process_content(content):

    chunk_size = 2000
    chunks = [content[i:i + chunk_size] for i in range(0, len(content), chunk_size)]
    docs = [Document(page_content=chunk) for chunk in chunks]

    return docs