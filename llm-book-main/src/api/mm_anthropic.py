import sys
import base64
import anthropic


def explain_image(filename: str) -> str:
    with open(filename, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode("utf-8")

    response = anthropic.Anthropic().messages.create(
        model="claude-3-5-sonnet-latest",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "この画像について説明してください。"},
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg",
                            "data": image_data,
                        },
                    },
                ],
            }
        ],
    )
    return response.content[0].text


answer = explain_image(sys.argv[1])
print(answer)
