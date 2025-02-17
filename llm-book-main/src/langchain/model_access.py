from langchain_openai import ChatOpenAI
# from langchain_anthropic import ChatAnthropic

llm = ChatOpenAI()
# llm = ChatAnthropic(model="claude-3-5-haiku-latest")

response = llm.invoke("あなたは何という言語モデルですか？")
print(response.content)
