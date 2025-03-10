import requests
import lxml
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
empire = response.text

soup = BeautifulSoup(empire, "lxml")
titles = soup.find_all(name="h2")
title_text = [title.text for title in titles]
with open("top 100 movies.txt", "a", encoding='utf-8') as file:
    for n in range(len(title_text)-1, 0, -1):
        file.write(f"{title_text[n]}\n")

