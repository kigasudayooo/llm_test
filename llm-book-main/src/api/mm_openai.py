import sys
import base64
from openai import OpenAI


def explain_image(filename: str) -> str:
    with open(filename, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode("utf-8")

    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "この画像について説明してください。"},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{image_data}"},
                    },
                ],
            }
        ],
    )
    return response.choices[0].message.content


answer = explain_image(sys.argv[1])
print(answer)
