from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template(
    "以下を日本語に翻訳してください。\n{input}"
)
llm = ChatOpenAI()
parser = StrOutputParser()

prompt = prompt_template.invoke("Hello, World!")
response = llm.invoke(prompt)
answer = parser.invoke(response)

print(answer)
