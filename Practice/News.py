from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/news"
response = requests.get(url).text

document = BeautifulSoup(response, "html.parser")
# print(document)

articles = document.findAll(name="a", class_="titlelink")

# upvotes = document.find(name="span", class_="score")
# print(upvotes.string)
upvotes = document.findAll(name="span", class_="score")
# print(upvotes.string)

article_upvotes = [""]
article_titles = [""]
article_links = [""]

for score in upvotes:
	article_upvotes.append(score.string)

for i in articles:
	article_titles.append(i.string)
	article_links.append(i['href'])

for element in range(1, 16):
	print(element)
	print(f"TITLE :{article_titles[element]}")
	print(f"LINK :{article_links[element]}")
	print(f"Score : {article_upvotes[element]}")
	print()
