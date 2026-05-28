import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text, "html.parser")

books = soup.select("article.product_pod")

for book in books[:10]:
    title = book.select_one("h3 a")["title"]
    price = book.select_one(".price_color").get_text(strip=True)

    print(title)
    print(price)
    print("-" * 30)
