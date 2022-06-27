from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/sapphire-radeon-rx-6800-11305-02-20g/p/N82E16814202394?Item=N82E16814202394&cm_" \
      "sp=Homepage_SS-_-P4_14-202-394-_-05302022&quicklink=true"

result = requests.get(url)
# print(result.text)
document = BeautifulSoup(result.text, 'html.parser')
# print(document.prettify())

prices = document.find_all(text="$")
# print(prices)

parent = prices[0].parent
# print(parent)

strong = parent.find("strong")
print(strong.string)
