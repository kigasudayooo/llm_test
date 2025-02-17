from openai import OpenAI

client = OpenAI()


# メッセージの設定
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "こんにちは。"},
]

try:
    # APIリクエストの送信
    response = client.chat.completions.create(model="gpt-4o-mini", messages=messages)

    # 応答の解析と利用
    assistant_reply = response.choices[0].message.content
    print("Assistant:", assistant_reply)

except Exception as e:
    # エラーハンドリング
    print(f"An error occurred: {e}")
