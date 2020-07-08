from bs4 import BeautifulSoup
from urllib.request import urlopen

# urlopen returns a bytes object
html = urlopen(
	"https://morvanzhou.github.io/static/scraping/list.html"
	).read().decode('utf-8')

# use lxml as the interpreter
soup = BeautifulSoup(html, features='lxml')

# add search by attribute
print("Find month li: ")
months = soup.find_all('li', {"class": "month"})
for m in months:
	print(m.get_text())

print("\nFind li under jan: ")
jan = soup.find('ul', {"class": "jan"})
date = jan.find_all('li')
for d in date:
	print(d.get_text())
