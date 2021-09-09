import requests
import numpy as np
import pandas as pd
from time import sleep
from random import randint
from bs4 import BeautifulSoup as bs

# set some display settings for notebooks
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# req_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}
req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

url = 'https://www.zillow.com/homes/San-Jose,-CA_rb/'

with requests.Session() as s:
    city = 'san-jose-ca'

    url1 = 'https://www.zillow.com/'+city+'/1_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22San%20Jose%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.41471486914062%2C%22east%22%3A-121.33530813085937%2C%22south%22%3A36.97251819044095%2C%22north%22%3A37.64383616047898%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A33839%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D'
    url2 = 'https://www.zillow.com/'+city+'/2_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22San%20Jose%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.41471486914062%2C%22east%22%3A-121.33530813085937%2C%22south%22%3A36.97251819044095%2C%22north%22%3A37.64383616047898%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A33839%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D'
    url3 = 'https://www.zillow.com/'+city+'/3_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22San%20Jose%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.41471486914062%2C%22east%22%3A-121.33530813085937%2C%22south%22%3A36.97251819044095%2C%22north%22%3A37.64383616047898%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A33839%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D'
    url4 = 'https://www.zillow.com/'+city+'/4_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22San%20Jose%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.41471486914062%2C%22east%22%3A-121.33530813085937%2C%22south%22%3A36.97251819044095%2C%22north%22%3A37.64383616047898%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A33839%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D'
    url5 = 'https://www.zillow.com/'+city+'/5_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22San%20Jose%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.41471486914062%2C%22east%22%3A-121.33530813085937%2C%22south%22%3A36.97251819044095%2C%22north%22%3A37.64383616047898%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A33839%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D'
    url6 = 'https://www.zillow.com/'+city+'/6_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22San%20Jose%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.41471486914062%2C%22east%22%3A-121.33530813085937%2C%22south%22%3A36.97251819044095%2C%22north%22%3A37.64383616047898%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A33839%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D'
    url7 = 'https://www.zillow.com/'+city+'/7_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22San%20Jose%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.41471486914062%2C%22east%22%3A-121.33530813085937%2C%22south%22%3A36.97251819044095%2C%22north%22%3A37.64383616047898%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A33839%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D'
    url8 = 'https://www.zillow.com/'+city+'/8_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22San%20Jose%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.41471486914062%2C%22east%22%3A-121.33530813085937%2C%22south%22%3A36.97251819044095%2C%22north%22%3A37.64383616047898%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A33839%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D'
    url9 = 'https://www.zillow.com/'+city+'/9_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22San%20Jose%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.41471486914062%2C%22east%22%3A-121.33530813085937%2C%22south%22%3A36.97251819044095%2C%22north%22%3A37.64383616047898%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A33839%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D'
    url10 = 'https://www.zillow.com/'+city+'/10_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22San%20Jose%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.41471486914062%2C%22east%22%3A-121.33530813085937%2C%22south%22%3A36.97251819044095%2C%22north%22%3A37.64383616047898%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A33839%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D'
    url11 = 'https://www.zillow.com/'+city+'/11_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22San%20Jose%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.41471486914062%2C%22east%22%3A-121.33530813085937%2C%22south%22%3A36.97251819044095%2C%22north%22%3A37.64383616047898%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A33839%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D'
    url12 = 'https://www.zillow.com/'+city+'/12_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22San%20Jose%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.41471486914062%2C%22east%22%3A-121.33530813085937%2C%22south%22%3A36.97251819044095%2C%22north%22%3A37.64383616047898%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A33839%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D'
    url13 = 'https://www.zillow.com/'+city+'/13_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22San%20Jose%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.41471486914062%2C%22east%22%3A-121.33530813085937%2C%22south%22%3A36.97251819044095%2C%22north%22%3A37.64383616047898%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A33839%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D'
    url14 = 'https://www.zillow.com/'+city+'/14_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22San%20Jose%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.41471486914062%2C%22east%22%3A-121.33530813085937%2C%22south%22%3A36.97251819044095%2C%22north%22%3A37.64383616047898%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A33839%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D'
    url15 = 'https://www.zillow.com/'+city+'/15_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22San%20Jose%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.41471486914062%2C%22east%22%3A-121.33530813085937%2C%22south%22%3A36.97251819044095%2C%22north%22%3A37.64383616047898%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A33839%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D'
    url16 = 'https://www.zillow.com/'+city+'/16_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22San%20Jose%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.41471486914062%2C%22east%22%3A-121.33530813085937%2C%22south%22%3A36.97251819044095%2C%22north%22%3A37.64383616047898%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A33839%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D'
    url17 = 'https://www.zillow.com/'+city+'/17_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22San%20Jose%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.41471486914062%2C%22east%22%3A-121.33530813085937%2C%22south%22%3A36.97251819044095%2C%22north%22%3A37.64383616047898%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A33839%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D'

    r = s.get(url, headers=req_headers)
    r2 = s.get(url, headers=req_headers)
    r3 = s.get(url, headers=req_headers)
    r4 = s.get(url, headers=req_headers)
    r5 = s.get(url, headers=req_headers)
    r6 = s.get(url, headers=req_headers)
    r7 = s.get(url, headers=req_headers)
    r8 = s.get(url, headers=req_headers)
    r9 = s.get(url, headers=req_headers)
    r10 = s.get(url, headers=req_headers)
    r11 = s.get(url, headers=req_headers)
    r12 = s.get(url, headers=req_headers)
    r13 = s.get(url, headers=req_headers)
    r14 = s.get(url, headers=req_headers)
    r15 = s.get(url, headers=req_headers)
    r16 = s.get(url, headers=req_headers)
    r17 = s.get(url, headers=req_headers)

    url_links = [ url1, url2, url3, url4, url5, url6, url7, url8, url9, 
                url10, url11, url12, url13, url14, url15, url16, url17, ]
    # print(url1)

# Add contents of urls to soup variable from the urls
soup1 = bs(r.content, 'html.parser')
soup2 = bs(r2.content, 'html.parser')
soup3 = bs(r3.content, 'html.parser')
soup4 = bs(r4.content, 'html.parser')
soup5 = bs(r5.content, 'html.parser')
soup6 = bs(r6.content, 'html.parser')
soup7 = bs(r7.content, 'html.parser')
soup8 = bs(r8.content, 'html.parser')
soup9 = bs(r9.content, 'html.parser')
soup10 = bs(r10.content, 'html.parser')
soup11 = bs(r11.content, 'html.parser')
soup12 = bs(r12.content, 'html.parser')
soup13 = bs(r13.content, 'html.parser')
soup14 = bs(r14.content, 'html.parser')
soup15 = bs(r15.content, 'html.parser')
soup16 = bs(r16.content, 'html.parser')
soup17 = bs(r17.content, 'html.parser')

# print(soup1)

df = pd.DataFrame()
df2 = pd.DataFrame()

for i in soup1:
    address = soup1.find_all (class_='list-card-addr')
    price = list(soup1.find_all (class_='list-card-price'))
    beds = list(soup1.find_all ("ul", class_='list-card-details'))
    details = soup1.find_all ('div', {'class': 'list-card-details'})

    # create dataframe columns
    df['prices'] = price
    df['beds'] = beds
    df['address'] = address

# url list
urls = []

# Check each article
for link in soup1.find_all("article"):
    href = link.find('a', class_="list-card-link")
    if href == None:
        addresses = None
    else:
        addresses = href.find('address',class_="list-card-addr").get_text()
        # print(addresses)
        urls.append(addresses)
        urls = [x for x in urls if x is not None]

# import url into a links column
df['links'] = urls
df['links'] = df['links'].astype('str')

# # remove html tags
# df['links'] = df['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
# df['links'] = df['links'].replace('" tabindex="0"></a>', ' ', regex=True)


#----------------------- 2nd page ----------------------------------
for i in soup2:
    soup = soup2
    address2 = soup2.find_all (class_='list-card-addr')
    price2 = list(soup2.find_all (class_='list-card-price'))
    beds2 = list(soup2.find_all ("ul", class_='list-card-details'))
    details2 = soup2.find_all ('div', {'class': 'list-card-details'})

    # create dataframe columns
    df['prices'] = price2
    df['beds'] = beds2
    df['address'] = address2

# url list
urls = []

# Check each article
for link in soup2.find_all("article"):
    href = link.find('a', class_="list-card-link")
    if href == None:
        addresses = None
    else:
        addresses = href.find('address',class_="list-card-addr").get_text()
        # print(addresses)
        urls.append(addresses)
        urls = [x for x in urls if x is not None]

# import url into a links column
df2['links'] = urls
df2['links'] = df2['links'].astype('str')

# remove html tags
df2['links'] = df['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df2['links'] = df['links'].replace('" tabindex="0"></a>', ' ', regex=True)


df = df.append(df2, ignore_index = True)

#create empty dataframes with panda
df3 = pd.DataFrame()
df4 = pd.DataFrame()
df5 = pd.DataFrame()
df6 = pd.DataFrame()
df7 = pd.DataFrame()
df8 = pd.DataFrame()
df9 = pd.DataFrame()
df10 = pd.DataFrame()
df11 = pd.DataFrame()
df12 = pd.DataFrame()
df13 = pd.DataFrame()
df14 = pd.DataFrame()
df15 = pd.DataFrame()
df16 = pd.DataFrame()
df17 = pd.DataFrame()

#----------------------- 3rd page ----------------------------------
for i in soup3:
    soup = soup3
    address3 = soup3.find_all (class_='list-card-addr')
    price3 = list(soup3.find_all (class_='list-card-price'))
    beds3 = list(soup3.find_all ("ul", class_='list-card-details'))
    details3 = soup3.find_all ('div', {'class': 'list-card-details'})

    # create dataframe columns
    df3['prices'] = price3
    df3['beds'] = beds3
    df3['address'] = address3

# url list
urls = []

# Check each article
for link in soup3.find_all("article"):
    href = link.find('a', class_="list-card-link")
    if href == None:
        addresses = None
    else:
        addresses = href.find('address',class_="list-card-addr").get_text()
        # print(addresses)
        urls.append(addresses)
        urls = [x for x in urls if x is not None]

# import url into a links column
df3['links'] = urls
df3['links'] = df3['links'].astype('str')

# remove html tags
df3['links'] = df3['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df3['links'] = df3['links'].replace('" tabindex="0"></a>', ' ', regex=True)

#----------------------- 4th page ----------------------------------
for i in soup4:
    soup = soup4
    address4 = soup4.find_all (class_='list-card-addr')
    price4 = list(soup4.find_all (class_='list-card-price'))
    beds4 = list(soup4.find_all ("ul", class_='list-card-details'))
    details4 = soup4.find_all ('div', {'class': 'list-card-details'})

    # create dataframe columns
    df4['prices'] = price4
    df4['beds'] = beds4
    df4['address'] = address4

# url list
urls = []

# Check each article
for link in soup4.find_all("article"):
    href = link.find('a', class_="list-card-link")
    if href == None:
        addresses = None
    else:
        addresses = href.find('address',class_="list-card-addr").get_text()
        # print(addresses)
        urls.append(addresses)
        urls = [x for x in urls if x is not None]

# import url into a links column
df4['links'] = urls
df4['links'] = df4['links'].astype('str')

# remove html tags
df4['links'] = df4['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df4['links'] = df4['links'].replace('" tabindex="0"></a>', ' ', regex=True)

#----------------------- 5th page ----------------------------------
for i in soup5:
    soup = soup5
    address5 = soup5.find_all (class_='list-card-addr')
    price5 = list(soup5.find_all (class_='list-card-price'))
    beds5 = list(soup5.find_all ("ul", class_='list-card-details'))
    details5 = soup5.find_all ('div', {'class': 'list-card-details'})

    # create dataframe columns
    df5['prices'] = price5
    df5['beds'] = beds5
    df5['address'] = address5

# url list
urls = []

# Check each article
for link in soup5.find_all("article"):
    href = link.find('a', class_="list-card-link")
    if href == None:
        addresses = None
    else:
        addresses = href.find('address',class_="list-card-addr").get_text()
        # print(addresses)
        urls.append(addresses)
        urls = [x for x in urls if x is not None]

# import url into a links column
df5['links'] = urls
df5['links'] = df5['links'].astype('str')

# remove html tags
df5['links'] = df5['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df5['links'] = df5['links'].replace('" tabindex="0"></a>', ' ', regex=True)

#----------------------- 6th page ----------------------------------
for i in soup6:
    soup = soup6
    address6 = soup6.find_all (class_='list-card-addr')
    price6 = list(soup6.find_all (class_='list-card-price'))
    beds6 = list(soup6.find_all ("ul", class_='list-card-details'))
    details6 = soup6.find_all ('div', {'class': 'list-card-details'})

    # create dataframe columns
    df6['prices'] = price6
    df6['beds'] = beds6
    df6['address'] = address6

# url list
urls = []

# Check each article
for link in soup6.find_all("article"):
    href = link.find('a', class_="list-card-link")
    if href == None:
        addresses = None
    else:
        addresses = href.find('address',class_="list-card-addr").get_text()
        # print(addresses)
        urls.append(addresses)
        urls = [x for x in urls if x is not None]

# import url into a links column
df6['links'] = urls
df6['links'] = df6['links'].astype('str')

# remove html tags
df6['links'] = df6['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df6['links'] = df6['links'].replace('" tabindex="0"></a>', ' ', regex=True)

#----------------------- 7th page ----------------------------------
for i in soup7:
    soup = soup7
    address7 = soup7.find_all (class_='list-card-addr')
    price7 = list(soup7.find_all (class_='list-card-price'))
    beds7 = list(soup7.find_all ("ul", class_='list-card-details'))
    details7 = soup7.find_all ('div', {'class': 'list-card-details'})

    # create dataframe columns
    df7['prices'] = price7
    df7['beds'] = beds7
    df7['address'] = address7

# url list
urls = []

# Check each article
for link in soup7.find_all("article"):
    href = link.find('a', class_="list-card-link")
    if href == None:
        addresses = None
    else:
        addresses = href.find('address',class_="list-card-addr").get_text()
        # print(addresses)
        urls.append(addresses)
        urls = [x for x in urls if x is not None]

# import url into a links column
df7['links'] = urls
df7['links'] = df7['links'].astype('str')

# remove html tags
df7['links'] = df7['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df7['links'] = df7['links'].replace('" tabindex="0"></a>', ' ', regex=True)

#----------------------- 8th page ----------------------------------
for i in soup8:
    soup = soup8
    address8 = soup8.find_all (class_='list-card-addr')
    price8 = list(soup8.find_all (class_='list-card-price'))
    beds8 = list(soup8.find_all ("ul", class_='list-card-details'))
    details8 = soup8.find_all ('div', {'class': 'list-card-details'})

    # create dataframe columns
    df8['prices'] = price8
    df8['beds'] = beds8
    df8['address'] = address8

# url list
urls = []

# Check each article
for link in soup8.find_all("article"):
    href = link.find('a', class_="list-card-link")
    if href == None:
        addresses = None
    else:
        addresses = href.find('address',class_="list-card-addr").get_text()
        # print(addresses)
        urls.append(addresses)
        urls = [x for x in urls if x is not None]

# import url into a links column
df8['links'] = urls
df8['links'] = df8['links'].astype('str')

# remove html tags
df8['links'] = df8['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df8['links'] = df8['links'].replace('" tabindex="0"></a>', ' ', regex=True)

#----------------------- 9th page ----------------------------------
for i in soup9:
    soup = soup9
    address9 = soup9.find_all (class_='list-card-addr')
    price9 = list(soup9.find_all (class_='list-card-price'))
    beds9 = list(soup9.find_all ("ul", class_='list-card-details'))
    details9 = soup9.find_all ('div', {'class': 'list-card-details'})

    # create dataframe columns
    df9['prices'] = price9
    df9['beds'] = beds9
    df9['address'] = address9

# url list
urls = []

# Check each article
for link in soup9.find_all("article"):
    href = link.find('a', class_="list-card-link")
    if href == None:
        addresses = None
    else:
        addresses = href.find('address',class_="list-card-addr").get_text()
        # print(addresses)
        urls.append(addresses)
        urls = [x for x in urls if x is not None]

# import url into a links column
df9['links'] = urls
df9['links'] = df9['links'].astype('str')

# remove html tags
df9['links'] = df9['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df9['links'] = df9['links'].replace('" tabindex="0"></a>', ' ', regex=True)

#----------------------- 10th page ----------------------------------
for i in soup10:
    soup = soup10
    address10 = soup10.find_all (class_='list-card-addr')
    price10 = list(soup10.find_all (class_='list-card-price'))
    beds10 = list(soup10.find_all ("ul", class_='list-card-details'))
    details10 = soup10.find_all ('div', {'class': 'list-card-details'})

    # create dataframe columns
    df10['prices'] = price10
    df10['beds'] = beds10
    df10['address'] = address10

# url list
urls = []

# Check each article
for link in soup10.find_all("article"):
    href = link.find('a', class_="list-card-link")
    if href == None:
        addresses = None
    else:
        addresses = href.find('address',class_="list-card-addr").get_text()
        # print(addresses)
        urls.append(addresses)
        urls = [x for x in urls if x is not None]

# import url into a links column
df10['links'] = urls
df10['links'] = df10['links'].astype('str')

# remove html tags
df10['links'] = df10['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df10['links'] = df10['links'].replace('" tabindex="0"></a>', ' ', regex=True)

#----------------------- 11th page ----------------------------------
for i in soup11:
    soup = soup11
    address11 = soup11.find_all (class_='list-card-addr')
    price11 = list(soup11.find_all (class_='list-card-price'))
    beds11 = list(soup11.find_all ("ul", class_='list-card-details'))
    details11 = soup11.find_all ('div', {'class': 'list-card-details'})

    # create dataframe columns
    df11['prices'] = price11
    df11['beds'] = beds11
    df11['address'] = address11

# url list
urls = []

# Check each article
for link in soup11.find_all("article"):
    href = link.find('a', class_="list-card-link")
    if href == None:
        addresses = None
    else:
        addresses = href.find('address',class_="list-card-addr").get_text()
        # print(addresses)
        urls.append(addresses)
        urls = [x for x in urls if x is not None]

# import url into a links column
df11['links'] = urls
df11['links'] = df11['links'].astype('str')

# remove html tags
df11['links'] = df11['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df11['links'] = df11['links'].replace('" tabindex="0"></a>', ' ', regex=True)

#----------------------- 12th page ----------------------------------
for i in soup12:
    soup = soup12
    address12 = soup12.find_all (class_='list-card-addr')
    price12 = list(soup12.find_all (class_='list-card-price'))
    beds12 = list(soup12.find_all ("ul", class_='list-card-details'))
    details12 = soup12.find_all ('div', {'class': 'list-card-details'})

    # create dataframe columns
    df12['prices'] = price12
    df12['beds'] = beds12
    df12['address'] = address12

# url list
urls = []

# Check each article
for link in soup12.find_all("article"):
    href = link.find('a', class_="list-card-link")
    if href == None:
        addresses = None
    else:
        addresses = href.find('address',class_="list-card-addr").get_text()
        # print(addresses)
        urls.append(addresses)
        urls = [x for x in urls if x is not None]

# import url into a links column
df12['links'] = urls
df12['links'] = df12['links'].astype('str')

# remove html tags
df12['links'] = df12['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df12['links'] = df12['links'].replace('" tabindex="0"></a>', ' ', regex=True)

#----------------------- 13th page ----------------------------------
for i in soup13:
    soup = soup13
    address13 = soup13.find_all (class_='list-card-addr')
    price13 = list(soup13.find_all (class_='list-card-price'))
    beds13 = list(soup13.find_all ("ul", class_='list-card-details'))
    details13 = soup13.find_all ('div', {'class': 'list-card-details'})

    # create dataframe columns
    df13['prices'] = price13
    df13['beds'] = beds13
    df13['address'] = address13

# url list
urls = []

# Check each article
for link in soup13.find_all("article"):
    href = link.find('a', class_="list-card-link")
    if href == None:
        addresses = None
    else:
        addresses = href.find('address',class_="list-card-addr").get_text()
        # print(addresses)
        urls.append(addresses)
        urls = [x for x in urls if x is not None]

# import url into a links column
df13['links'] = urls
df13['links'] = df13['links'].astype('str')

# remove html tags
df13['links'] = df13['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df13['links'] = df13['links'].replace('" tabindex="0"></a>', ' ', regex=True)
14
#----------------------- 14th page ----------------------------------
for i in soup14:
    soup = soup14
    address14 = soup14.find_all (class_='list-card-addr')
    price14 = list(soup14.find_all (class_='list-card-price'))
    beds14 = list(soup14.find_all ("ul", class_='list-card-details'))
    details14 = soup14.find_all ('div', {'class': 'list-card-details'})

    # create dataframe columns
    df14['prices'] = price14
    df14['beds'] = beds14
    df14['address'] = address14

# url list
urls = []

# Check each article
for link in soup14.find_all("article"):
    href = link.find('a', class_="list-card-link")
    if href == None:
        addresses = None
    else:
        addresses = href.find('address',class_="list-card-addr").get_text()
        # print(addresses)
        urls.append(addresses)
        urls = [x for x in urls if x is not None]

# import url into a links column
df14['links'] = urls
df14['links'] = df14['links'].astype('str')

# remove html tags
df14['links'] = df14['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df14['links'] = df14['links'].replace('" tabindex="0"></a>', ' ', regex=True)

#----------------------- 15th page ----------------------------------
for i in soup15:
    soup = soup15
    address15 = soup15.find_all (class_='list-card-addr')
    price15 = list(soup15.find_all (class_='list-card-price'))
    beds15 = list(soup15.find_all ("ul", class_='list-card-details'))
    details15 = soup15.find_all ('div', {'class': 'list-card-details'})

    # create dataframe columns
    df15['prices'] = price15
    df15['beds'] = beds15
    df15['address'] = address15

# url list
urls = [] 

# Check each article
for link in soup15.find_all("article"):
    href = link.find('a', class_="list-card-link")
    if href == None:
        addresses = None
    else:
        addresses = href.find('address',class_="list-card-addr").get_text()
        # print(addresses)
        urls.append(addresses)
        urls = [x for x in urls if x is not None]

# import url into a links column
df15['links'] = urls
df15['links'] = df15['links'].astype('str')

# remove html tags
df15['links'] = df15['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df15['links'] = df15['links'].replace('" tabindex="0"></a>', ' ', regex=True)

#----------------------- 16th page ----------------------------------
for i in soup16:
    soup = soup16
    address16 = soup16.find_all (class_='list-card-addr')
    price16 = list(soup16.find_all (class_='list-card-price'))
    beds16 = list(soup16.find_all ("ul", class_='list-card-details'))
    details16 = soup16.find_all ('div', {'class': 'list-card-details'})

    # create dataframe columns
    df16['prices'] = price16
    df16['beds'] = beds16
    df16['address'] = address16

# url list
urls = []

# Check each article
for link in soup16.find_all("article"):
    href = link.find('a', class_="list-card-link")
    if href == None:
        addresses = None
    else:
        addresses = href.find('address',class_="list-card-addr").get_text()
        # print(addresses)
        urls.append(addresses)
        urls = [x for x in urls if x is not None]

# import url into a links column
df16['links'] = urls
df16['links'] = df16['links'].astype('str')

# remove html tags
df16['links'] = df16['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df16['links'] = df16['links'].replace('" tabindex="0"></a>', ' ', regex=True)

#----------------------- 17th page ----------------------------------
for i in soup17:
    soup = soup17
    address17 = soup17.find_all (class_='list-card-addr')
    price17 = list(soup17.find_all (class_='list-card-price'))
    beds17 = list(soup17.find_all ("ul", class_='list-card-details'))
    details17 = soup17.find_all ('div', {'class': 'list-card-details'})

    # create dataframe columns
    df17['prices'] = price17
    df17['beds'] = beds17
    df17['address'] = address17

# url list
urls = []

# Check each article
for link in soup17.find_all("article"):
    href = link.find('a', class_="list-card-link")
    if href == None:
        addresses = None
    else:
        addresses = href.find('address',class_="list-card-addr").get_text()
        # print(addresses)
        urls.append(addresses)
        urls = [x for x in urls if x is not None]

# import url into a links column
df17['links'] = urls
df17['links'] = df17['links'].astype('str')

# remove html tags
df17['links'] = df17['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df17['links'] = df17['links'].replace('" tabindex="0"></a>', ' ', regex=True)

df = df.append(df3, ignore_index = True)
df = df.append(df4, ignore_index = True)
df = df.append(df5, ignore_index = True)
df = df.append(df6, ignore_index = True)
df = df.append(df7, ignore_index = True)
df = df.append(df8, ignore_index = True)
df = df.append(df9, ignore_index = True)
df = df.append(df10, ignore_index = True)
df = df.append(df11, ignore_index = True)
df = df.append(df12, ignore_index = True)
df = df.append(df13, ignore_index = True)
df = df.append(df14, ignore_index = True)
df = df.append(df15, ignore_index = True)
df = df.append(df16, ignore_index = True)
df = df.append(df17, ignore_index = True)

#convert columns to str
df['prices'] = df['prices'].astype('str')
df['address'] = df['address'].astype('str')
df['beds'] = df['beds'].astype('str')

#remove html tags
df['prices'] = df['prices'].replace('<div class="list-card-price">', ' ', regex=True)
df['address'] = df['address'].replace('<address class="list-card-addr">', ' ', regex=True)
df['prices'] = df['prices'].replace('</div>', ' ', regex=True)
df['address'] = df['address'].replace('</address>', ' ', regex=True)
df['prices'] = df['prices'].str.replace(r'\D', '')

#remove html tags from beds column
df['beds'] = df['beds'].replace('<ul class="list-card-details"><li>', ' ', regex=True)
df['beds'] = df['beds'].replace('<abbr class="list-card-label"> <!-- -->bds</abbr></li><li>', ' ', regex=True)
df['beds'] = df['beds'].replace('<abbr class="list-card-label"> <!-- -->ba</abbr></li><li>', ' ', regex=True)
df['beds'] = df['beds'].replace('<abbr class="list-card-label"> <!-- -->bd</abbr></li><li>', ' ', regex=True)
df['beds'] = df['beds'].replace('<abbr class="list-card-label"> <!-- -->sqft</abbr></li></ul>', ' ', regex=True)
df['beds'] = df['beds'].replace('Studio</li><li>', '0 ', regex=True)

#split beds column into beds, bath and sq_feet
df[['beds','baths','sq_feet']] = df.beds.str.split(expand=True)

#remove commas from sq_feet and convert to float
df.replace(',','', regex=True, inplace=True)

#drop nulls
df = df[(df['prices'] != '') & (df['prices']!= ' ')]

#convert column to float
df['prices'] = df['prices'].astype('float')
# df['sq_feet'] = df['sq_feet'].astype('float')

print('The column datatypes are:')
print(df.dtypes)
print('The dataframe shape is:', df.shape)

#rearrange the columns
df = df[['prices', 'address', 'links', 'beds', 'baths', 'sq_feet']]

# soup = bs(r.text, 'html.parser')

# overText = []
# propType = []
# propID = []
# zipCd = []
# priceMain = []
# bd = []
# ba = []
# sqFt = []
# address = []


# container = soup.find_all('article', {'class': 'list-card'})

# pages = np.arrange(1,50,1)

# # For each page
# for page in pages:
#     page = requests.get("https://www.zillow.com/san-jose-ca/"+str(page)+"_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22San%20Jose%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.41471486914062%2C%22east%22%3A-121.33530813085937%2C%22south%22%3A36.97251819044095%2C%22north%22%3A37.64383616047898%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A33839%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D")
#     soup = bs(page.text, "html-parser")
#     container = soup.find_all('article', attrs={'class': 'list-card'})
#     sleep(randint(2,8))

#     # For each item
#     for store in container:
#         price = store.find('div', {'class': 'list-card-price'}).text
#         priceMain.append(price)


# for item in container:
#     price = item.find('div', {'class': 'list-card-price'}).text
#     price = item.find('div', {'class': 'list-card-price'}).text
#     price = item.find('div', {'class': 'list-card-price'}).text
#     price = item.find('div', {'class': 'list-card-price'}).text
#     price = item.find('div', {'class': 'list-card-price'}).text
#     bedroom = item.find(class_='list-card-details').find_next_sibling().text.strip()
#     print(bedroom)


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

