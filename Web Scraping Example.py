# Make sure you have installed bs4 and requests using pip
# Dont worry if this code does not work, we have not discussed this yet
from bs4 import BeautifulSoup
import requests
link = "https://www.marvel.com/comics/characters"
page = requests.get(link)
soup = BeautifulSoup(page.content, 'html.parser')
result = soup.find_all('li')
for i in result:
	print(i.a.text + "---" + "https://www.marvel.com" + i.a['href'])
