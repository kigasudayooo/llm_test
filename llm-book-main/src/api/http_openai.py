import requests
import json
import os

# OpenAI API の設定
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

# ヘッダーの設定
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}"
}

# リクエストの内容
data = {
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "こんにちは。"}
    ]
}

# 1. HTTPリクエスト（POST）の送信
response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))

# 4. HTTP応答（JSON）の受信
if response.status_code == 200:
    # 5. 応答の解析と利用
    result = response.json()
    assistant_reply = result['choices'][0]['message']['content']
    print("Assistant:", assistant_reply)
else:
    print("Error:", response.status_code, response.text)
