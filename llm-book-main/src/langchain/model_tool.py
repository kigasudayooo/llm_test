from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, ToolMessage
from langchain_core.tools import tool

llm = ChatOpenAI()

messages = [
    SystemMessage("あなたの名前はハルです。"),
    HumanMessage("私の名前はデイブです。"),
    AIMessage("こんにちは、デイブさん。"),
    HumanMessage("ハル、ポッドのライトを20度左にまわしてくれ。"),
]


@tool
def light_control(degrees: float) -> bool:
    """
    ライトを右に degrees 度回します。
    """
    # ここでライトを右に degrees 度回すコードを実装する
    print(f"light_control: {degrees}")
    return True


llm_with_tool = llm.bind_tools([light_control])
response = llm_with_tool.invoke(messages)
messages.append(response)
if response.tool_calls:
    for call in response.tool_calls:
        value = light_control.invoke(call["args"])
        messages.append(ToolMessage(value, tool_call_id=call["id"]))
response = llm_with_tool.invoke(messages)
print(response.content)
