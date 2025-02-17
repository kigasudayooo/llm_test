from langchain_openai import ChatOpenAI

llm = ChatOpenAI()

messages = llm.batch(
    [
        "おはようございます。",
        "こんにちは。",
        "こんばんは。",
    ]
)
for message in messages:
    print(message.content)
