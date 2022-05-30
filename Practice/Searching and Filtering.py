from bs4 import BeautifulSoup
import re

with open("index2.html", 'r') as file:
	document = BeautifulSoup(file, "html.parser")

# print(document.find('option'))
# print(f"{document.find_all('option')}")

# tags = document.find_all(['p'])

# tags = document.find_all(class_='btn-item')

# tags = document.find_all(text=re.compile("\$.*

tags = document.find_all(text=re.compile("\$.*"), limit=1)
print(tags)
