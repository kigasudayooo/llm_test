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

text = input("User: ")

prompt = translation_prompt.invoke({"input": text, "language": "English"})
ai_message = llm.invoke(prompt)
answer = parser.invoke(ai_message)

print("AI:", answer)
