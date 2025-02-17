import streamlit as st
from typing import TypedDict, List
from pyaskit import function


# TypedDictを使用してクイズの形式を定義します。
class Quiz(TypedDict):
    question: str  # 問題文
    choices: List[str]  # 選択肢
    model_answer: int  # 正解の選択肢のインデックス


@function(codable=False)
def make_quiz(category: str, n: int, count: int, difficulty: int) -> List[Quiz]:
    """{{category}}分野から{{count}}個の{{n}}択問題（question）、
    選択肢（choices）、模範解答（model_answer）を日本語で作成してください。
    模範解答の選択肢の番号は0 から {{n}}-1とします。
    難易度は{{difficulty}}とします。1が最も簡単で10が最も難しいです。"""


st.title("クイズアプリ")  # アプリのタイトルを設定

# ユーザにカテゴリを入力してもらいます。
category = st.text_input("カテゴリを入力してください:", value="プログラミング")

# 選択肢の数を選んでもらいます。
n_choices = st.slider("選択肢の数:", min_value=3, max_value=5, value=4)

# 難易度を選んでもらいます。
difficulty = st.slider("難易度:", min_value=1, max_value=10, value=5)

# 問題数を選んでもらいます。
question_count = st.slider("問題数:", min_value=1, max_value=10, value=5)

# セッション状態にクイズがなければ初期化します。
if "quizzes" not in st.session_state:
    st.session_state.quizzes = []

# クイズを生成するボタン
if st.button("クイズを生成"):
    # クイズを生成してセッション状態に保存します。
    quizzes = make_quiz(category, n_choices, question_count, difficulty)
    st.session_state.quizzes = quizzes
    # ユーザの解答を格納するリストを初期化します。
    st.session_state.user_answers = [0] * len(quizzes)

# クイズと選択肢を表示します。
for i, quiz in enumerate(st.session_state.quizzes):
    st.write(f"Q{i+1}: {quiz['question']}")
    options = quiz["choices"]
    # 選択肢のラジオボタンを表示します。
    answer = st.radio("選択肢:", options, key=f"question_{i}")
    # ユーザの解答を更新します。
    st.session_state.user_answers[i] = options.index(answer)

# 採点するボタン
if st.button("採点"):
    score = 0
    # 正解数を数えます。
    for i, quiz in enumerate(st.session_state.quizzes):
        if quiz["model_answer"] == st.session_state.user_answers[i]:
            score += 1
    # スコアを表示します。
    st.write(f"スコア: {score}/{len(st.session_state.quizzes)}")
    # 正解を表示します。
    st.write("正解:")
    for i, quiz in enumerate(st.session_state.quizzes):
        st.write(f"Q{i+1}: {quiz['choices'][quiz['model_answer']]}")
