'''
Printa list of all the article titles on the New York Times homepage to txt file
'''

import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.nytimes.com/")
soup = BeautifulSoup(response.text, "html.parser")

# with open('21_Write-to-a-file.txt','w') as file:
with open('21_Write-to-a-file.txt','w') as file:
	for el in  soup.select(".esl82me2"): #list
		file.write(el.get_text()+ '\n')


