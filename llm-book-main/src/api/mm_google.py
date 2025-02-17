import sys
import google.generativeai as genai
import PIL.Image


def explain_image(filename: str):
    model = genai.GenerativeModel("gemini-1.5-flash-latest")
    response = model.generate_content(
        contents=[
            {
                "role": "user",
                "parts": [
                    "この画像について説明してください。",
                    PIL.Image.open(filename),
                ],
            }
        ]
    )
    return response.text


answer = explain_image(sys.argv[1])
print(answer)
