import requests
from bs4 import BeautifulSoup

url = 'https://www.zillow.com/homes/San-Jose,-CA_rb/'

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
lists = soup.find_all('article', class_="list-card")

for list in lists:
    price = lists.find_all('a', class_="list-card-price")
    address = lists.find_all('address', class_="list-card-addr")

    # Bedroom
    bedDiv = soup.find('div', {'class': 'list-card-details'})
    bedNumber = bedDiv.find()

    # Bathroom
    price = lists.find_all('a', class_="list-card-price")
    price = lists.find_all('a', class_="list-card-price")

