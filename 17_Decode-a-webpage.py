'''
Print out a list of all the article titles on the New York Times homepage
'''

import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.nytimes.com/")
soup = BeautifulSoup(response.text, "html.parser")

for el in  soup.select(".esl82me2"): #list
	print(el.get_text())
