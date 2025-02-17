from langchain_core.prompts import PromptTemplate


prompt_template = PromptTemplate.from_template("{planet}の情報を教えてください。")
prompt = prompt_template.invoke({"planet": "金星"})
print(prompt)
