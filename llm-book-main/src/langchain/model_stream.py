from langchain_openai import ChatOpenAI

llm = ChatOpenAI()

for chunk in llm.stream("こんにちは"):
    print(chunk.content, end="", flush=True)
