import requests
from bs4 import BeautifulSoup

url = "https://www.totalcorner.com/match/today"

page = requests.get( url, cookies=cookies)
soup = BeautifulSoup(page.content, 'html.parser')
print( soup.prettify() )
