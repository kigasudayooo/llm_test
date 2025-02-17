from langchain_community.document_loaders import PyPDFLoader
import requests
import os

url = "https://www.soumu.go.jp/johotsusintokei/whitepaper/ja/r05/pdf/00zentai.pdf"
filename = "情報通信白書.pdf"

if not os.path.exists(filename):
    with open(filename, "wb") as file:
        file.write(requests.get(url).content)

loader = PyPDFLoader(filename)
pages = loader.load()
print(f"ページ数: {len(pages)}")
n = 100
print(f"{n}ページ目： {pages[n].page_content[:100]}")
