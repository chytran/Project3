import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as bs

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}
url = 'https://www.zillow.com/homes/San-Jose,-CA_rb/'
r = requests.get(url, headers=headers)
soup = bs(r.text, 'html.parser')

prices = soup.find_all('div', {'class': 'list-card-price'})

for item in prices:
    



# lists = soup.find_all('article', class_="list-card")

# page = 1
# titles = []
# while page != 18:
#     url = 'https://www.zillow.com/homes/San-Jose,-CA_rb/'
#     # url = "https://www.zillow.com/san-jose-ca/{page}_p/?searchQueryState=%7B%22usersSearchTerm%22%3A%22San%20Jose%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-124.90861135351562%2C%22east%22%3A-121.34354787695312%2C%22south%22%3A36.468806825690045%2C%22north%22%3A38.43661600149848%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A33839%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22category%22%3A%22cat1%22%2C%22mapZoom%22%3A9%7D"
#     response = requests.get(url)
#     html = response.content
#     soup = bs(html, "lxml")
#     for h3 in soup.find_all("div", class_="list-card-price"):
#         titles.append(h3.get_text(strip=True))
#     page = page + 1

# print(len(titles))
# for list in lists:
#     price = lists.find_all('a', class_="list-card-price")
#     address = lists.find_all('address', class_="list-card-addr")

#     # Bedroom
#     bedDiv = soup.find('div', {'class': 'list-card-details'})
#     bedNumber = bedDiv.find()

#     # Bathroom
#     overviewText = lists.find_all('a', class_="list-card-price")
#     propertyType = lists.find_all('a', class_="list-card-price")
#     propertyID = lists.find_all('a', class_="list-card-price")
#     address = lists.find_all('a', class_="list-card-price")
#     zipCode = lists.find_all('a', class_="list-card-price")
#     squareFt = lists.find_all('a', class_="list-card-price")

