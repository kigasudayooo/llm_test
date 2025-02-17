from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough

translation_prompt = PromptTemplate.from_template(
    "次の文章を{language}に翻訳し、"
    "翻訳された文章だけ答えてください：\n"
    "```\n"
    "{input}\n"
    "```"
)

llm = ChatOpenAI(model="gpt-4o-mini")

translation = translation_prompt | llm | StrOutputParser()

to_english = {
    "input": RunnablePassthrough(),
    "language": lambda _: "English",
} | translation

to_japanese = {
    "input": RunnablePassthrough(),
    "language": lambda _: "Japanese",
} | translation

chain = to_english | llm | StrOutputParser() | to_japanese
text = input("User: ")
answer = chain.invoke(text)
print(answer)
