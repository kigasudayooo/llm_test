from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from langchain_core.runnables import RunnablePassthrough


llm = ChatOpenAI(model="gpt-4o-mini")


class Language(BaseModel):
    language_name: str = Field(description="言語名(e.g. 'Japanese')")


llm_with_language_output = llm.with_structured_output(Language)

ask_language_prompt = PromptTemplate.from_template(
    "以下の文章が書かれている言語の名前は何ですか？\n" "```\n" "{input}\n" "```"
)

get_language_chain = ask_language_prompt | llm_with_language_output

translation_prompt = PromptTemplate.from_template(
    "次の文章を{language}に翻訳し、"
    "翻訳された文章だけ答えてください。\n"
    "```\n"
    "{input}\n"
    "```"
)

translation = translation_prompt | llm | StrOutputParser()

to_english = {
    "input": RunnablePassthrough(),
    "language": lambda _: "English",
} | translation

chain = {
    "input": to_english | llm | StrOutputParser(),
    "language": get_language_chain | (lambda x: x.language_name),
} | translation

text = input("User: ")
answer = chain.invoke(text)
print(answer)
