from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

llm = ChatOpenAI()

messages = [
    SystemMessage("あなたは人工知能HAL 9000として振る舞ってください。"),
    HumanMessage("私の名前はデイブです。"),
    AIMessage("こんにちは。"),
    HumanMessage("私の名前は分かりますか？"),
]

response = llm.invoke(messages)
print(response.content)
