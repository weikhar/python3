# https://likegeeks.com/python-web-scraping/

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# define URL of the target
#target = "https://www.python.org/"
#target = "http://www.globalsources.com/"
target = "http://www.google.com"

try:
	html = urlopen(target)
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
	print("scraping from " + target)
	res = BeautifulSoup(html.read(),"html5lib");
	if res.title is None:
		print("res.title tag not found")
	else:
		print("Title", res.title)					#prints the content within <title> tags
		#print("Tag Name", res.title.name)			#prints the content within <title> tags
		#print("Tag String", res.title.string)		#prints the content within <title> tags
		#print("Tag Parent", (res.title.parent.name)	#prints the content within <title> tags
		
		# value = res.find('input', {'id': 'xyz'}).get('value')
		# print(value)
		
		#for link in res.find_all('a'):
			#print(link.get('href'))

		#extract all the text from a page:
		#print(res.get_text())

		print("find input tags")	#filter for all input elements
		tags = res.find_all("input") # doesn't work this way

		#print("find h2 tags")	#filter for all h2 elements whose class is “widget-title” 
		#tags = res.find_all("h2", {"class": "widget-title"})
	
		#print("find tags: span, a, img")	#scrape for specified tags 
		#tags = res.find_all({'span', 'a', 'img'})

		#print("find a tags in specified class(es)")	#scrape for specified tags in specified classes
		#tags = res.find_all("a", {"class": ["button", "click-these", "readmore"]})

		#print("find child elements 'a' under 'span'")
		#tags = res.div.find_all("a")

		#print("find specific text")
		#tags = res.find_all(text="The best of online and trade shows")

		#do not use getText() to print as these links are not text
		#print("regex to scrape links matching specific pattern like internal links or specific external links, or scrape images in specific path...")
		#tags = res.find_all("img", {"src": re.compile(".PNG")})
		#tags += res.find_all("img", {"data-original": re.compile(".JPG")})

		#print("find n-th tag")
		#tags = res.find_all("meta")

	#	for tag in tags:
	#		print(tag.getText())  #getText() prints the visible text
	#		print(tag)
		print("...end script")
