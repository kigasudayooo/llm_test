from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    HumanMessagePromptTemplate,
)
from langchain_core.messages import SystemMessage
from operator import itemgetter


filename = "情報通信白書.pdf"
loader = PyPDFLoader(filename)
pages = loader.load()

python_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=400)
splits = python_splitter.split_documents(pages)

persist_directory = "db"
vectorstore = Chroma.from_documents(
    documents=splits,
    embedding=OpenAIEmbeddings(model="text-embedding-3-small"),
    persist_directory=persist_directory,
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

prompt_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage("あなたは有能なアシスタントです。"),
        MessagesPlaceholder("chat_history"),
        HumanMessagePromptTemplate.from_template(
            "与えられた文脈に基づいて、次の質問に答えてください。\n文脈：{context}\n質問：{question}"
        ),
    ]
)


llm = ChatOpenAI(temperature=0)


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


rag_chain = (
    {
        "context": itemgetter("question") | retriever | format_docs,
        "question": itemgetter("question"),
        "chat_history": itemgetter("chat_history"),
    }
    | prompt_template
    | llm
    | StrOutputParser()
)

history = []
answer = rag_chain.invoke({"question": "生成AIの最新動向は？", "chat_history": history})
print(answer)
