from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


translation_prompt = PromptTemplate.from_template(
    "次の文章を{language}に翻訳し、"
    "翻訳された文章だけ答えてください。\n"
    "```\n"
    "{input}\n"
    "```"
)

llm = ChatOpenAI(model="gpt-4o-mini")

parser = StrOutputParser()

translation = translation_prompt | llm | parser

text = input("User: ")

answer = translation.invoke({"input": text, "language": "English"})

print("AI:", answer)
