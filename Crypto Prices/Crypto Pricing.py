from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"

result = requests.get(url).text
document = BeautifulSoup(result, "html.parser")

# print(document)

table_body = document.tbody
# print(table_body)
table_rows = table_body.contents
# print(table_rows)
# print(table_rows[0])
# print(table_rows[0].next_sibling)
# print(table_rows[0].next_siblings)

# crypto_table = list(table_rows[0].next_siblings)
# for element in crypto_table:
# 	print(element)

# print(list(table_rows[0].descendants))

crypto_prices = {}

for tr in table_rows[:10]:
	name, price = tr.contents[2:4]
	# print(name.p.string)
	fixed_name = name.p.string
	# print(price.a.string)
	fixed_price = price.a.string

	crypto_prices[fixed_name] = fixed_price

print(crypto_prices)
