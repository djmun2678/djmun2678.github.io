import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import os
import subprocess
import time

WAIT_TIME = 300

url = "https://books.toscrape.com/"

def clean_filename(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9가-힣]+", "-", text)
    return text.strip("-")

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.select("article.product_pod")

os.makedirs("content/posts", exist_ok=True)

for i, book in enumerate(books[:5], start=1):
    title = book.select_one("h3 a")["title"]
    price = book.select_one(".price_color").get_text(strip=True)
    stock = book.select_one(".availability").get_text(strip=True)
    rating = book.select_one("p")["class"][1]

    filename = clean_filename(title)
    today = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+09:00")

    md_content = f"""---
title: "{title}"
date: {today}
draft: false
---

# {title}

## 책 정보

- 가격: {price}
- 재고: {stock}
- 평점: {rating}

## 정리

이 글은 자동으로 생성된 책 리뷰 글입니다.
"""

    file_path = f"content/posts/{filename}.md"

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(md_content)

    print(f"{i}번째 글 저장 완료: {title}")

    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", f"add book post {i}"], check=True)
    subprocess.run(["git", "push"], check=True)

    print(f"{i}번째 글 GitHub 업로드 완료")

    if i < 5:
        print("5분 기다리는 중...")
        time.sleep(WAIT_TIME)

print("총 5개 글 업로드 완료!")