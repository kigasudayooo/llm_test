from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

filename = "情報通信白書.pdf"
loader = PyPDFLoader(filename)
pages = loader.load()

python_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=400)
splits = python_splitter.split_documents(pages)
print(f"チャンク数：{len(splits)}")
n = 100
print(f"{n}チャンク目：{splits[n].page_content[:100]}")
