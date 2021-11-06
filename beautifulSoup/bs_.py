# https://programminghistorian.org/en/lessons/retired/intro-to-beautiful-soup
from bs4 import BeautifulSoup
import requests

url = "http://www.google.com" 

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

#print nicely indented html
# print(soup.prettify())

links = soup.find_all('a')

for link in links:
    print(link.contents[0])
    print(link.get('href'))