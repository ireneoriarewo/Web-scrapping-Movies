import json
import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
movies_webpage = response.text
soup = BeautifulSoup(movies_webpage, "html.parser")
data = json.loads(soup.select_one(selector="#__NEXT_DATA__").contents[0])

movies = []

data_dict = data["props"]["pageProps"]["apolloState"]
for a, b in data_dict.items():
    if a.startswith("ImageMeta"):
        try:
            list = b["titleText"]
        except KeyError:
            pass
        movies.append(list)

top100 = movies[::-1]
with open('movies.txt', mode="w") as file:
    for movie in top100:
        file.write(f"{movie}\n")
