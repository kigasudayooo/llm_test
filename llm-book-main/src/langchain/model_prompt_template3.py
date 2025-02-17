from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage
from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)


chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template("あなたの名前は{ai_name}です。"),
        HumanMessagePromptTemplate.from_template("私の名前は{human_name}です。"),
        AIMessage("こんにちは。"),
        HumanMessagePromptTemplate.from_template("{input}"),
    ]
)

prompt = chat_template.invoke(
    {
        "ai_name": "SAL 9000",
        "human_name": "ヘイウッド",
        "input": "私の名前は分かりますか？",
    }
)
print(prompt)

llm = ChatOpenAI()
response = llm.invoke(prompt)
print(response.content)
