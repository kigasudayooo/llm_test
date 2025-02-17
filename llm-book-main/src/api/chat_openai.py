from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "最も古いプログラミング言語は？"},
        {
            "role": "assistant",
            "content": "最も古いプログラミング言語の一つは、1950年代初頭に開発されたFORTRANです。",
        },
        {"role": "user", "content": "誰が開発しましたか？"},
    ],
    temperature=0.7,
    top_p=0.9,
    max_tokens=150,
    stop=["。", "."],
)

latest_response = response.choices[0].message.content
print(latest_response)
