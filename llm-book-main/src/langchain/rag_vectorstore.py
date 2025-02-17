from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

filename = "情報通信白書.pdf"
loader = PyPDFLoader(filename)
pages = loader.load()

python_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=400)
splits = python_splitter.split_documents(pages)

vectorstore = Chroma.from_documents(
    documents=splits, embedding=OpenAIEmbeddings(model="text-embedding-3-small")
)
docs = vectorstore.similarity_search("生成AIの最新動向は？", k=3)
for doc in docs:
    print("---")
    print(doc.page_content[:100])
