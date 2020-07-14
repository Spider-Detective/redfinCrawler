from bs4 import BeautifulSoup
from urllib.request import urlopen

# urlopen returns a bytes object
html = urlopen(
	"https://morvanzhou.github.io/static/scraping/basic-structure.html"
	).read().decode('utf-8')
# use lxml as the interpreter
soup = BeautifulSoup(html, features='lxml')
print(soup.h1)
all_href = soup.find_all('a')
all_href = [l['href'] for l in all_href] # access attributes in all_href
print('\n', all_href)