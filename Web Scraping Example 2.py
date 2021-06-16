from bs4 import BeautifulSoup
import requests
link = "https://personaldevelopfit.com/motivational-quotes/"
page = requests.get(link)
soup = BeautifulSoup(page.content, "html.parser")
result = soup.find_all('blockquote')
for i in result:
	print(i.text)


