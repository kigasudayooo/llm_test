import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from operator import itemgetter


# ドキュメントを整形
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


# チェーンを作成
def create_chain():
    vectorstore = Chroma(
        embedding_function=OpenAIEmbeddings(model="text-embedding-3-small"),
        persist_directory="data",
    )
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "回答には以下の情報も参考にしてください。参考情報：\n{info}",
            ),
            ("placeholder", "{history}"),
            ("human", "{input}"),
        ]
    )
    return (
        {
            "input": itemgetter("input"),
            "info": itemgetter("input") | retriever | format_docs,
            "history": itemgetter("history"),
        }
        | prompt
        | ChatOpenAI(model="gpt-4o-mini", temperature=0)
    )


# セッション状態を初期化
if "history" not in st.session_state:
    st.session_state.history = []
    st.session_state.chain = create_chain()

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
    response = st.session_state.chain.invoke(
        {
            "input": user_input,
            "history": st.session_state.history,
        }
    )
    st.session_state.history.append(HumanMessage(user_input))
    st.session_state.history.append(response)

    # 会話を表示
    for message in reversed(st.session_state.history):
        st.write(f"{message.type}: {message.content}")
