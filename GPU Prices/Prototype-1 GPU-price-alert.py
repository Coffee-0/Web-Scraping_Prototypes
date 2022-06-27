from bs4 import BeautifulSoup
import requests
import re

item = input("What are you looking for : ")

url = f"https://www.newegg.com/p/pl?d={item}&N=8000%204131"
page = requests.get(url).text
document = BeautifulSoup(page, "html.parser")

page_text = document.find(class_="list-tool-pagination-text").strong
# print(page_text)
page_number = int(str(page_text).split("/")[-2].split(">")[-1][:-1])
# print(page_number)

items_found = {}

for page in range(1, page_number + 1):
	url = f"https://www.newegg.com/p/pl?d={item}&N=8000%204131&page={page}"
	page_ = requests.get(url).text
	document = BeautifulSoup(page_, "html.parser")
	div = document.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")

	items = div.find_all(text=re.compile(item))

	# for i in items:
	# 	parent = i.parent
	# 	link = None
	# 	if parent.name == 'a':
	# 		link = parent['href']
	#
	# 	print(link)

	for i in items:
		parent = i.parent
		link = None
		if parent.name != "a":
			continue
		link = parent['href']
		next_parent = i.find_parent(class_="item-container")
		price = next_parent.find(class_="price-current").strong.string
		# print(price)

		items_found[i] = {"price": int(price.replace(",", "")), "link": link}

print(items_found)
