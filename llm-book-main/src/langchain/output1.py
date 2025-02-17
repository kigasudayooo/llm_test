from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import Literal


class CelestialBody(BaseModel):
    name: str = Field(description="天体の名前（漢字表記）")
    radius: float = Field(description="天体の半径（km）")
    mass: float = Field(description="天体の質量（kg）")
    type: Literal["恒星", "惑星", "衛星"] = Field(description="天体の種類")


llm = ChatOpenAI()
llm_with_structured_output = llm.with_structured_output(CelestialBody)
jupiter = llm_with_structured_output.invoke("木星の情報を教えてください。")
print(f"木星の半径: {jupiter.radius} km")
print(f"木星の質量: {jupiter.mass} kg")
print(f"木星の種類: {jupiter.type}")
