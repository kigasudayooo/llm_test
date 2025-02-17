import streamlit as st
from langchain_openai import ChatOpenAI

st.title("マルチモーダルRAGチャットボット")

# アップローダを追加
uploaded_file = st.file_uploader("画像を選択してください", type=["jpg", "jpeg", "png"])

# アップロードされた画像を表示
if uploaded_file is not None:
    st.image(uploaded_file, caption="画像", width=300)


# ユーザ入力を受け取る
user_input = st.text_input("メッセージを入力してください:")

# ボタンを追加し、クリックされたらアクションを起こす
if st.button("送信"):
    # OpenAIの言語モデルを使って応答を生成
    llm = ChatOpenAI()
    response = llm.invoke(user_input)

    # 会話を表示
    st.write(f"ai: {response.content}")
    st.write(f"human: {user_input}")
