from urllib.request import urlopen
import re

print("-------------------\n")
print("This is the first version of my web crawler:\n")
# urlopen returns a bytes object
html = urlopen(
	"https://morvanzhou.github.io/static/scraping/basic-structure.html"
	).read().decode('utf-8')
# need to decode the bytes object before using regex
title = re.findall(r"<title>(.*)</title>", html)
p = re.findall(r"<p>(.*)</p>", html, flags=re.DOTALL) # flags is for multi-line
anchors = re.findall(r'href="(.*)"', html)
print("\nPage title is: ", title[0])
print("\nPage paragraph is: ", p[0])
print("\nPage links are: ", anchors)