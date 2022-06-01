from bs4 import BeautifulSoup
import requests

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url).text

document = BeautifulSoup(response, "html.parser")
titles = document.findAll(name="div", class_="article-title-description__text")
# print(titles.find_all(class_="title"))
# title_movies = (titles.find(class_="title"))
# print(title_movies.string.split(")")[1])

title_movies = []
for i in titles:
	title_movies.append((i.find(class_="title")))

# print(title_movies)
movies = []
for movie in title_movies:
	movies.append(movie.string)

# print(movies)

with open("Movies.txt", "a") as file:
	for film in movies:
		file.write(f"{film}\n")
