import google.generativeai as genai


config = genai.types.GenerationConfig(
    temperature=0.7,
    top_p=0.9,
    max_output_tokens=150,
    stop_sequences=["。", "."],
)

model = genai.GenerativeModel("gemini-1.5-flash-latest")
response = model.generate_content(
    contents=[
        {
            "role": "user",
            "parts": ["最も古いプログラミング言語はなんですか？"],
        },
        {
            "role": "model",
            "parts": [
                "最も古いプログラミング言語の一つは、1950年代初頭に開発されたFORTRANです。"
            ],
        },
        {"role": "user", "parts": ["誰が開発しましたか？"]},
    ],
    generation_config=config,
)

latest_response = response.text
print(latest_response)
