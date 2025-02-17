from langchain_openai import ChatOpenAI
# from langchain_anthropic import ChatAnthropic
# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

llm = ChatOpenAI(model="gpt-4o-mini")
# llm = ChatAnthropic(model="claude-3-5-haiku-latest")
# llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")

messages = [
    # SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="最も古いプログラミング言語はなんですか？"),
    AIMessage(
        content="最も古いプログラミング言語の一つは、1950年代初頭に開発されたFORTRANです。"
    ),
    HumanMessage(content="誰が開発しましたか？"),
]

response = llm.invoke(messages)

# 最新のアシスタントの応答を取得して表示
latest_response = response.content
print(latest_response)
