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

req_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}
url = 'https://www.zillow.com/homes/San-Jose,-CA_rb/'

with requests.Session() as s:
    city = 'san-jose-ca'

    urll = 'https://www.zillow.com/'+city+'/1_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22San%20Jose%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.41471486914062%2C%22east%22%3A-121.33530813085937%2C%22south%22%3A36.97251819044095%2C%22north%22%3A37.64383616047898%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A33839%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D'
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

    url_links = [ urll, url2, url3, url4, url5, url6, url7, url8, url9, 
                url10, url11, url12, url13, url14, url15, url16, url17, ]
    print(url_links)

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
    addresses = href.find('address') #find address tag
    addresses.extract()
    urls.append(href)

# import url into a links column
df['links'] = urls
df['links'] = df['links'].astype('str')

# remove html tags
df['links'] = df['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df['links'] = df['links'].replace('" tabindex="0"></a>', ' ', regex=True)


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
    addresses = href.find('address') #find address tag
    addresses.extract()
    urls.append(href)

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
    addresses = href.find('address') #find address tag
    addresses.extract()
    urls.append(href)

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
    addresses = href.find('address') #find address tag
    addresses.extract()
    urls.append(href)

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
    addresses = href.find('address') #find address tag
    addresses.extract()
    urls.append(href)

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
    addresses = href.find('address') #find address tag
    addresses.extract()
    urls.append(href)

# import url into a links column
df6['links'] = urls
df6['links'] = df6['links'].astype('str')

# remove html tags
df6['links'] = df6['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df6['links'] = df6['links'].replace('" tabindex="0"></a>', ' ', regex=True)

#----------------------- 7th page ----------------------------------
for i in soup3:
    soup = soup7
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
    addresses = href.find('address') #find address tag
    addresses.extract()
    urls.append(href)

# import url into a links column
df3['links'] = urls
df3['links'] = df3['links'].astype('str')

# remove html tags
df3['links'] = df3['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df3['links'] = df3['links'].replace('" tabindex="0"></a>', ' ', regex=True)

#----------------------- 8th page ----------------------------------
for i in soup3:
    soup = soup8
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
    addresses = href.find('address') #find address tag
    addresses.extract()
    urls.append(href)

# import url into a links column
df3['links'] = urls
df3['links'] = df3['links'].astype('str')

# remove html tags
df3['links'] = df3['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df3['links'] = df3['links'].replace('" tabindex="0"></a>', ' ', regex=True)

#----------------------- 9th page ----------------------------------
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
    addresses = href.find('address') #find address tag
    addresses.extract()
    urls.append(href)

# import url into a links column
df3['links'] = urls
df3['links'] = df3['links'].astype('str')

# remove html tags
df3['links'] = df3['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df3['links'] = df3['links'].replace('" tabindex="0"></a>', ' ', regex=True)

#----------------------- 10th page ----------------------------------
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
    addresses = href.find('address') #find address tag
    addresses.extract()
    urls.append(href)

# import url into a links column
df3['links'] = urls
df3['links'] = df3['links'].astype('str')

# remove html tags
df3['links'] = df3['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df3['links'] = df3['links'].replace('" tabindex="0"></a>', ' ', regex=True)

#----------------------- 11th page ----------------------------------
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
    addresses = href.find('address') #find address tag
    addresses.extract()
    urls.append(href)

# import url into a links column
df3['links'] = urls
df3['links'] = df3['links'].astype('str')

# remove html tags
df3['links'] = df3['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df3['links'] = df3['links'].replace('" tabindex="0"></a>', ' ', regex=True)

#----------------------- 12th page ----------------------------------
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
    addresses = href.find('address') #find address tag
    addresses.extract()
    urls.append(href)

# import url into a links column
df3['links'] = urls
df3['links'] = df3['links'].astype('str')

# remove html tags
df3['links'] = df3['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df3['links'] = df3['links'].replace('" tabindex="0"></a>', ' ', regex=True)

#----------------------- 13th page ----------------------------------
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
    addresses = href.find('address') #find address tag
    addresses.extract()
    urls.append(href)

# import url into a links column
df3['links'] = urls
df3['links'] = df3['links'].astype('str')

# remove html tags
df3['links'] = df3['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df3['links'] = df3['links'].replace('" tabindex="0"></a>', ' ', regex=True)

#----------------------- 14th page ----------------------------------
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
    addresses = href.find('address') #find address tag
    addresses.extract()
    urls.append(href)

# import url into a links column
df3['links'] = urls
df3['links'] = df3['links'].astype('str')

# remove html tags
df3['links'] = df3['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df3['links'] = df3['links'].replace('" tabindex="0"></a>', ' ', regex=True)

#----------------------- 15th page ----------------------------------
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
    addresses = href.find('address') #find address tag
    addresses.extract()
    urls.append(href)

# import url into a links column
df3['links'] = urls
df3['links'] = df3['links'].astype('str')

# remove html tags
df3['links'] = df3['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df3['links'] = df3['links'].replace('" tabindex="0"></a>', ' ', regex=True)

#----------------------- 16th page ----------------------------------
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
    addresses = href.find('address') #find address tag
    addresses.extract()
    urls.append(href)

# import url into a links column
df3['links'] = urls
df3['links'] = df3['links'].astype('str')

# remove html tags
df3['links'] = df3['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df3['links'] = df3['links'].replace('" tabindex="0"></a>', ' ', regex=True)

#----------------------- 17th page ----------------------------------
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
    addresses = href.find('address') #find address tag
    addresses.extract()
    urls.append(href)

# import url into a links column
df3['links'] = urls
df3['links'] = df3['links'].astype('str')

# remove html tags
df3['links'] = df3['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df3['links'] = df3['links'].replace('" tabindex="0"></a>', ' ', regex=True)








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

