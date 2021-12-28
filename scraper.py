import requests
from bs4 import BeautifulSoup


url = "/page/1"
all_quote = []
while url:
    print(f"processing {url}")
    res = requests.get(f"http://quotes.toscrape.com{url}")
    soup = BeautifulSoup(res.text,"html.parser")
    quotes = soup.find_all(class_="quote")
    for quote in quotes:
        all_quote.append({"text":quote.find(class_="text").get_text(), "author":quote.find(class_="author").get_text(),  "about":quote.find("a")["href"]})
    next_button = soup.find(class_="next")
    url = next_button.find("a")["href"] if next_button else None
print(all_quote)

