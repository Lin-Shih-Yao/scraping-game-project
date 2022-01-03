import requests
from bs4 import BeautifulSoup
from random import choice

# 處理資料
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
# 處理邏輯
remaining_guesses = 4 
question = choice(all_quote)
print(question["text"])
guess = ""
while guess.lower() != question["author"].lower() and remaining_guesses > 0:
    guess = input(f"pleas answer the author: you have only {remaining_guesses} chance ")
    remaining_guesses -= 1
    # 猜對的邏輯
    if guess.lower() == question["author"].lower():
        print("you got a author")
        break
    # 猜錯的邏輯
    if remaining_guesses == 3:
        url = question["about"]
        res = requests.get(f"http://quotes.toscrape.com{url}")
        soup = BeautifulSoup(res.text,"html.parser")
        birth = soup.find(class_="author-born-date").get_text()
        location = soup.find(class_="author-born-location").get_text()
        print(f"Here's a hint : The author was born on {birth} {location}")
    elif remaining_guesses == 2:
        hint2 = question["author"][0]
        print(f"The author first name is starts with {hint2}")
    elif remaining_guesses == 1:
        hint3 = question["author"].split()[-1][0]
        print(f"The author last name is starts with {hint3}")
    else:
        game_over = question["author"]
        print(f"Game over! The answer is {game_over}")

