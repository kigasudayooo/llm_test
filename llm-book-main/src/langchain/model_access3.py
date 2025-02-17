from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import sys
import base64


def explain_image(filename: str) -> str:
    with open(filename, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode("utf-8")
    llm = ChatOpenAI(model="gpt-4o-mini")

    message = HumanMessage(
        content=[
            {
                "type": "text",
                "text": "この画像について説明してください。",
            },
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{image_data}"},
            },
        ]
    )

    response = llm.invoke([message])
    return response.content


answer = explain_image(sys.argv[1])
print(answer)
