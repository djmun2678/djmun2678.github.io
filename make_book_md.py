import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import os
import subprocess
import time

WAIT_TIME = 300
BOOKS_DIR = "content/books"
BATCH_SIZE = 5

url = "https://books.toscrape.com/"


def clean_filename(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9가-힣]+", "-", text)
    return text.strip("-")


def safe_git(*args):
    """Run a git command; warn but don't crash if it fails."""
    try:
        subprocess.run(["git", *args], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"  [warn] git {' '.join(args)} 실패: {e}")
        return False


response = requests.get(url)
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text, "html.parser")

books = soup.select("article.product_pod")

os.makedirs(BOOKS_DIR, exist_ok=True)

for i, book in enumerate(books[:BATCH_SIZE], start=1):
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

    file_path = f"{BOOKS_DIR}/{filename}.md"

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(md_content)

    print(f"{i}번째 글 저장 완료: {title}")

    if safe_git("add", file_path) and safe_git("commit", "-m", f"add book post {i}: {title}"):
        safe_git("push")
        print(f"{i}번째 글 GitHub 업로드 완료")
    else:
        print(f"{i}번째 글 GitHub 업로드 건너뜀")

    if i < BATCH_SIZE:
        print(f"{WAIT_TIME // 60}분 기다리는 중...")
        time.sleep(WAIT_TIME)

print(f"총 {BATCH_SIZE}개 글 처리 완료!")
