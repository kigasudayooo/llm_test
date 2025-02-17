from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import AIMessage

message = AIMessage("こんにちは。")
s = "こんばんは。"

parser = StrOutputParser()
result1 = parser.invoke(message)
result2 = parser.invoke(s)

print(result1)
print(result2)
