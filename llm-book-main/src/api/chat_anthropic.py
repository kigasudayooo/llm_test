import anthropic

response = anthropic.Anthropic().messages.create(
    model="claude-3-5-haiku-latest",
    temperature=0.7,
    top_p=0.9,
    max_tokens=150,
    stop_sequences=["。", "."],
    messages=[
        {"role": "user", "content": "最も古いプログラミング言語はなんですか？"},
        {
            "role": "assistant",
            "content": "最も古いプログラミング言語の一つは、1950年代初頭に開発されたFORTRANです。",
        },
        {"role": "user", "content": "誰が開発しましたか？"},
    ],
)

latest_response = response.content[0].text
print(latest_response)
