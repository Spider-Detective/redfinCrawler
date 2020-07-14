from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random

base_url = "https://baike.baidu.com"
list = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]
visited = {""}

for i in range(20):
	url = base_url + list[-1]
	try:
		html = urlopen(url).read().decode('utf-8')
	except:
		print(i, ' Dead link, skip')
		list.pop()
		continue

	soup = BeautifulSoup(html, features='lxml')
	print(i, ' ', soup.find('h1').get_text(), '\turl: ', list[-1])

	sub_urls = soup.find_all("a", {"target": "_blank",
		                           "href": re.compile("/item/(%.{2})+$")})
	# pick 1 random link to proceed, if no link, go back
	if len(sub_urls) != 0:
		url = random.sample(sub_urls, 1)[0]['href']
		count = 1;
		# select a link have not been visited
		while (count <= len(sub_urls) and (url in visited)):
			url = random.sample(sub_urls, 1)[0]['href']
			count += 1

		if count > len(sub_urls):
			print(i, 'no new url, skip')
			list.pop()
			continue
		else:
			list.append(url)
			visited.add(url)
	else:
		print(i, 'End link, go back')
		list.pop()
	