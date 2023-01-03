import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
movies_web = response.text

# Create a list of the top 100 movies from the url provided above
soup = BeautifulSoup(movies_web, "html.parser")
titles = soup.find_all(name="h3", class_="title")
movies_list = []
for movie in titles:
    movie_title = movie.getText()
    movies_list.append(movie_title)


# Create a file with the top 100 movies
with open('movies.txt', 'w') as f:
    for movie in movies_list[::-1]:
        f.write(f"{movie}\n")
