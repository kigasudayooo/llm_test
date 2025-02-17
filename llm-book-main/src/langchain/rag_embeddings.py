from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings

filename = "情報通信白書.pdf"
loader = PyPDFLoader(filename)
pages = loader.load()

python_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=400)
splits = python_splitter.split_documents(pages)

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
content = splits[10].page_content
vector = embeddings.embed_query(content)
print(f"埋め込みベクトルの次元数: {len(vector)}")
print(f"埋め込みベクトルの最初の10要素: {vector[:10]}")
