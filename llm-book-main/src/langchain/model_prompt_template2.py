from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from typing import Literal


class CelestialBody(BaseModel):
    name: str = Field(description="天体の名前（漢字表記）")
    radius: float = Field(description="天体の半径（km）")
    mass: float = Field(description="天体の質量（kg）")
    type: Literal["恒星", "惑星", "衛星"] = Field(description="天体の種類")


llm = ChatOpenAI().with_structured_output(CelestialBody)
prompt_template = PromptTemplate.from_template("{planet}の情報を教えてください。")

venus = llm.invoke(prompt_template.invoke({"planet": "金星"}))
earth = llm.invoke(prompt_template.invoke({"planet": "地球"}))

print(f"金星の半径: {venus.radius} km")
print(f"地球の半径: {earth.radius} km")
