from bs4 import BeautifulSoup

with open("index.html", "r") as file:
	doc = BeautifulSoup(file, "html.parser")

"""
Read and print the complete HTML file : 

print(doc.prettify())

"""

"""
Accessing a specific tag :

tag = doc.title
print(tag)  # This will print '<title>BeautifulSoup</title>' 

"""

"""
Accessing only the content within the tags :

tag = doc.title
print(tag.string)

"""

"""
Modifying whats inside of tags :

tag = doc.title
tag.string = "Hello"  # This will change the content within title tag and replace it with 'hello'
print(tag)

"""

"""
Finding all tags with the tag name :
"""

tag = doc.find_all("p")
print(tag)
