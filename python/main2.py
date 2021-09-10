import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
import numpy as np
import pandas as pd
import regex as re
import requests
import lxml
from lxml.html.soupparser import fromstring
import prettify
import numbers
import htmltext
from IPython.display import display

#set some display settings for notebooks
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

#add headers in case you use chromedriver (captchas are no fun); namely used for chromedriver
req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

#create url variables for each zillow page
with requests.Session() as s:
    city = 'austin/' #*****change this city to what you want!!!!*****
    
    url = 'https://www.zillow.com/homes/for_sale/'+city
    url2 = 'https://www.zillow.com/homes/for_sale/'+city+'/2_p/'
    url3 = 'https://www.zillow.com/homes/for_sale/'+city+'/3_p/'
    url4 = 'https://www.zillow.com/homes/for_sale/'+city+'/4_p/'
    url5 = 'https://www.zillow.com/homes/for_sale/'+city+'/5_p/'
    url6 = 'https://www.zillow.com/homes/for_sale/'+city+'/6_p/'
    url7 = 'https://www.zillow.com/homes/for_sale/'+city+'/7_p/'
    url8 = 'https://www.zillow.com/homes/for_sale/'+city+'/8_p/'
    url9 = 'https://www.zillow.com/homes/for_sale/'+city+'/9_p/'
    url10 = 'https://www.zillow.com/homes/for_sale/'+city+'/10_p/'

    r = s.get(url, headers=req_headers)
    r2 = s.get(url2, headers=req_headers)
    r3 = s.get(url3, headers=req_headers)
    r4 = s.get(url4, headers=req_headers)
    r5 = s.get(url5, headers=req_headers)
    r6 = s.get(url6, headers=req_headers)
    r7 = s.get(url7, headers=req_headers)
    r8 = s.get(url8, headers=req_headers)
    r9 = s.get(url9, headers=req_headers)
    r10 = s.get(url10, headers=req_headers)
    
    url_links = [url, url2, url3, url4, url5, url6, url7, url8, url9, url10]

#add contents of urls to soup variable from each url
soup = BeautifulSoup(r.content, 'html.parser')
soup1 = BeautifulSoup(r2.content, 'html.parser')
soup2 = BeautifulSoup(r3.content, 'html.parser')
soup3 = BeautifulSoup(r4.content, 'html.parser')
soup4 = BeautifulSoup(r5.content, 'html.parser')
soup5 = BeautifulSoup(r6.content, 'html.parser')
soup6 = BeautifulSoup(r7.content, 'html.parser')
soup7 = BeautifulSoup(r8.content, 'html.parser')
soup8 = BeautifulSoup(r9.content, 'html.parser')
soup9 = BeautifulSoup(r10.content, 'html.parser')

# page_links = [soup, soup1, soup2, soup3, soup4, soup5, soup6, soup7, soup8, soup9]

#create the first two dataframes
df = pd.DataFrame()
df1 = pd.DataFrame()

#all for loops are pulling the specified variable using beautiful soup and inserting into said variable
for i in soup:
    address = soup.find_all (class_= 'list-card-addr')
    price = list(soup.find_all (class_='list-card-price'))
    beds = list(soup.find_all("ul", class_="list-card-details"))
    details = soup.find_all ('div', {'class': 'list-card-details'})
    home_type = soup.find_all ('div', {'class': 'list-card-footer'})
    last_updated = soup.find_all ('div', {'class': 'list-card-top'})
    brokerage = list(soup.find_all(class_= 'list-card-brokerage list-card-img-overlay',text=True))
    link = soup.find_all (class_= 'list-card-link')
    
    #create dataframe columns out of variables
    df['prices'] = price
    df['address'] = address
    df['beds'] = beds

#create empty url list
urls = []

#loop through url, pull the href and strip out the address tag
for link in soup.find_all("article"):
    href = link.find('a',class_="list-card-link")
#     print(href)
    if href == None:
        addresses = None
#         addresses = 'zillow doesnt like this piece of code!'
    else:
        addresses = href.find('address',class_="list-card-addr").get_text()
#     print(addresses)
#     addresses = addresses.get_text()
#     addresses = href.find_all(href=True)
#     addresses = href.find('address class')
#     addresses.extract()
#     print(addresses)
    urls.append(addresses)
    urls = [x for x in urls if x is not None]

df['links'] = urls
df['links'] = df['links'].astype('str')

#remove html tags
# df['links'] = df['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
# df['links'] = df['links'].replace('" tabindex="0"></a>', ' ', regex=True)

for i in soup1:
    address1 = soup1.find_all (class_= 'list-card-addr')
    price1 = list(soup1.find_all (class_='list-card-price'))
    beds1 = list(soup.find_all("ul", class_="list-card-details"))
    details1 = soup1.find_all ('div', {'class': 'list-card-details'})
    home_type1 = soup1.find_all ('div', {'class': 'list-card-footer'})
    last_updated1 = soup1.find_all ('div', {'class': 'list-card-top'})
    brokerage1 = list(soup1.find_all(class_= 'list-card-brokerage list-card-img-overlay',text=True))
    link1 = soup1.find_all (class_= 'list-card-link')
#     zestimate1 = soup1.find_all (class_= 'Text-c11n-8-38-0__aiai24-0 jtMauM')

    #create dataframe columns out of variables
    df1['prices'] = price1
    df1['address'] = address1
    df1['beds'] = beds
#     df1['zestimate'] = zestimate1

#create empty url list
urls = []

#loop through url, pull the href and strip out the address tag
for link in soup1.find_all("article"):
    href = link.find('a',class_="list-card-link")
    if href == None:
        addresses = None
    else:
        addresses = href.find('address',class_="list-card-addr").get_text()
    urls.append(addresses)
    urls = [x for x in urls if x is not None]

#import urls into a links column
df1['links'] = urls
df1['links'] = df1['links'].astype('str')

#remove html tags
# df1['links'] = df1['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
# df1['links'] = df1['links'].replace('" tabindex="0"></a>', ' ', regex=True)

#append first two dataframes
df = df.append(df1, ignore_index = True) 

#create empty dataframes
df2 = pd.DataFrame()
df3 = pd.DataFrame()
df4 = pd.DataFrame()
df5 = pd.DataFrame()
df6 = pd.DataFrame()
df7 = pd.DataFrame()
df8 = pd.DataFrame()
df9 = pd.DataFrame()

for i in soup2:
    soup = soup2
    address = soup.find_all (class_= 'list-card-addr')
    price = list(soup.find_all (class_='list-card-price'))
    beds = list(soup.find_all("ul", class_="list-card-details"))
    details = soup.find_all ('div', {'class': 'list-card-details'})
    home_type = soup.find_all ('div', {'class': 'list-card-footer'})
    last_updated = soup.find_all ('div', {'class': 'list-card-top'})
    brokerage = list(soup.find_all(class_= 'list-card-brokerage list-card-img-overlay',text=True))
    link = soup.find_all (class_= 'list-card-link')
    
    #create dataframe columns out of variables
    df2['prices'] = price
    df2['address'] = address
    df2['beds'] = beds

time.sleep(3.2)    

#create empty url list
urls = []

#loop through url, pull the href and strip out the address tag
for link in soup2.find_all("article"):
    href = link.find('a',class_="list-card-link")
    if href == None:
        addresses = None
    else:
        addresses = href.find('address',class_="list-card-addr").get_text()
    urls.append(addresses)
    urls = [x for x in urls if x is not None]

#import urls into a links column
df2['links'] = urls
df2['links'] = df2['links'].astype('str')

#remove html tags
# df2['links'] = df2['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
# df2['links'] = df2['links'].replace('" tabindex="0"></a>', ' ', regex=True)

#append n df
# df = df.append(df2, ignore_index = True) 
# display(df)
# time.sleep(3.1)

for i in soup3:
    soup = soup3
    address1 = soup.find_all (class_= 'list-card-addr')
    price1 = list(soup.find_all (class_='list-card-price'))
    beds1 = list(soup.find_all("ul", class_="list-card-details"))
    details1 = soup.find_all ('div', {'class': 'list-card-details'})
    home_type1 = soup.find_all ('div', {'class': 'list-card-footer'})
    last_updated1 = soup.find_all ('div', {'class': 'list-card-top'})
    brokerage1 = list(soup.find_all(class_= 'list-card-brokerage list-card-img-overlay',text=True))
    link1 = soup.find_all (class_= 'list-card-link')

    #create dataframe columns out of variables
    df3['prices'] = price1
    df3['address'] = address1
    df3['beds'] = beds

#create empty url list
urls = []

#loop through url, pull the href and strip out the address tag
for link in soup3.find_all("article"):
    href = link.find('a',class_="list-card-link")
    if href == None:
        addresses = None
    else:
        addresses = href.find('address',class_="list-card-addr").get_text()
    urls.append(addresses)
    urls = [x for x in urls if x is not None]

#import urls into a links column
df3['links'] = urls
df3['links'] = df3['links'].astype('str')

#remove html tags
# df3['links'] = df3['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
# df3['links'] = df3['links'].replace('" tabindex="0"></a>', ' ', regex=True)

for i in soup4:
    soup = soup4
    address1 = soup.find_all (class_= 'list-card-addr')
    price1 = list(soup.find_all (class_='list-card-price'))
    beds1 = list(soup.find_all("ul", class_="list-card-details"))
    details1 = soup.find_all ('div', {'class': 'list-card-details'})
    home_type1 = soup.find_all ('div', {'class': 'list-card-footer'})
    last_updated1 = soup.find_all ('div', {'class': 'list-card-top'})
    brokerage1 = list(soup.find_all(class_= 'list-card-brokerage list-card-img-overlay',text=True))
    link1 = soup.find_all (class_= 'list-card-link')

    #create dataframe columns out of variables
    df4['prices'] = price1
    df4['address'] = address1
    df4['beds'] = beds

#create empty url list
urls = []

#loop through url, pull the href and strip out the address tag
for link in soup4.find_all("article"):
    href = link.find('a',class_="list-card-link")
    if href == None:
        addresses = None
    else:
        addresses = href.find('address',class_="list-card-addr").get_text()
    urls.append(addresses)
    urls = [x for x in urls if x is not None]

#import urls into a links column
df4['links'] = urls
df4['links'] = df4['links'].astype('str')

#remove html tags
# df4['links'] = df4['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
# df4['links'] = df4['links'].replace('" tabindex="0"></a>', ' ', regex=True)

for i in soup5:
    soup = soup5
    address1 = soup.find_all (class_= 'list-card-addr')
    price1 = list(soup.find_all (class_='list-card-price'))
    beds1 = list(soup.find_all("ul", class_="list-card-details"))
    details1 = soup.find_all ('div', {'class': 'list-card-details'})
    home_type1 = soup.find_all ('div', {'class': 'list-card-footer'})
    last_updated1 = soup.find_all ('div', {'class': 'list-card-top'})
    brokerage1 = list(soup.find_all(class_= 'list-card-brokerage list-card-img-overlay',text=True))
    link1 = soup.find_all (class_= 'list-card-link')

    #create dataframe columns out of variables
    df5['prices'] = price1
    df5['address'] = address1
    df5['beds'] = beds

#create empty url list
urls = []

#loop through url, pull the href and strip out the address tag
for link in soup5.find_all("article"):
    href = link.find('a',class_="list-card-link")
    if href == None:
        addresses = None
    else:
        addresses = href.find('address',class_="list-card-addr").get_text()
    urls.append(addresses)
    urls = [x for x in urls if x is not None]

#import urls into a links column
df5['links'] = urls
df5['links'] = df5['links'].astype('str')

#remove html tags
# df5['links'] = df5['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
# df5['links'] = df5['links'].replace('" tabindex="0"></a>', ' ', regex=True)
    
for i in soup6:
    soup = soup6
    address1 = soup.find_all (class_= 'list-card-addr')
    price1 = list(soup.find_all (class_='list-card-price'))
    beds1 = list(soup.find_all("ul", class_="list-card-details"))
    details1 = soup.find_all ('div', {'class': 'list-card-details'})
    home_type1 = soup.find_all ('div', {'class': 'list-card-footer'})
    last_updated1 = soup.find_all ('div', {'class': 'list-card-top'})
    brokerage1 = list(soup.find_all(class_= 'list-card-brokerage list-card-img-overlay',text=True))
    link1 = soup.find_all (class_= 'list-card-link')

    #create dataframe columns out of variables
    df6['prices'] = price1
    df6['address'] = address1
    df6['beds'] = beds

#create empty url list
urls = []

#loop through url, pull the href and strip out the address tag
for link in soup6.find_all("article"):
    href = link.find('a',class_="list-card-link")
    if href == None:
        addresses = None
    else:
        addresses = href.find('address',class_="list-card-addr").get_text()
    urls.append(addresses)
    urls = [x for x in urls if x is not None]

time.sleep(3)

#import urls into a links column
df6['links'] = urls
df6['links'] = df6['links'].astype('str')

#remove html tags
# df6['links'] = df6['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
# df6['links'] = df6['links'].replace('" tabindex="0"></a>', ' ', regex=True)
    
for i in soup7:
    soup = soup7
    address1 = soup.find_all (class_= 'list-card-addr')
    price1 = list(soup.find_all (class_='list-card-price'))
    beds1 = list(soup.find_all("ul", class_="list-card-details"))
    details1 = soup.find_all ('div', {'class': 'list-card-details'})
    home_type1 = soup.find_all ('div', {'class': 'list-card-footer'})
    last_updated1 = soup.find_all ('div', {'class': 'list-card-top'})
    brokerage1 = list(soup.find_all(class_= 'list-card-brokerage list-card-img-overlay',text=True))
    link1 = soup.find_all (class_= 'list-card-link')

    #create dataframe columns out of variables
    df7['prices'] = price1
    df7['address'] = address1
    df7['beds'] = beds

#create empty url list
urls = []

#loop through url, pull the href and strip out the address tag
for link in soup7.find_all("article"):
    href = link.find('a',class_="list-card-link")
    if href == None:
        addresses = None
    else:
        addresses = href.find('address',class_="list-card-addr").get_text()
    urls.append(addresses)
    urls = [x for x in urls if x is not None]

#import urls into a links column
df7['links'] = urls
df7['links'] = df7['links'].astype('str')

#remove html tags
# df7['links'] = df7['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
# df7['links'] = df7['links'].replace('" tabindex="0"></a>', ' ', regex=True)
    
for i in soup8:
    soup = soup8
    address1 = soup.find_all (class_= 'list-card-addr')
    price1 = list(soup.find_all (class_='list-card-price'))
    beds1 = list(soup.find_all("ul", class_="list-card-details"))
    details1 = soup.find_all ('div', {'class': 'list-card-details'})
    home_type1 = soup.find_all ('div', {'class': 'list-card-footer'})
    last_updated1 = soup.find_all ('div', {'class': 'list-card-top'})
    brokerage1 = list(soup.find_all(class_= 'list-card-brokerage list-card-img-overlay',text=True))
    link1 = soup.find_all (class_= 'list-card-link')

    #create dataframe columns out of variables
    df8['prices'] = price1
    df8['address'] = address1
    df8['beds'] = beds

#create empty url list
urls = []

#loop through url, pull the href and strip out the address tag
for link in soup8.find_all("article"):
    href = link.find('a',class_="list-card-link")
    if href == None:
        addresses = None
    else:
        addresses = href.find('address',class_="list-card-addr").get_text()
    urls.append(addresses)
    urls = [x for x in urls if x is not None]

#import urls into a links column
df8['links'] = urls
df8['links'] = df8['links'].astype('str')

#remove html tags
# df8['links'] = df8['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
# df8['links'] = df8['links'].replace('" tabindex="0"></a>', ' ', regex=True)

for i in soup9:
    soup = soup9
    address1 = soup.find_all (class_= 'list-card-addr')
    price1 = list(soup.find_all (class_='list-card-price'))
    beds1 = list(soup.find_all("ul", class_="list-card-details"))
    details1 = soup.find_all ('div', {'class': 'list-card-details'})
    home_type1 = soup.find_all ('div', {'class': 'list-card-footer'})
    last_updated1 = soup.find_all ('div', {'class': 'list-card-top'})
    brokerage1 = list(soup.find_all(class_= 'list-card-brokerage list-card-img-overlay',text=True))
    link1 = soup.find_all (class_= 'list-card-link')

    #create dataframe columns out of variables
    df9['prices'] = price1
    df9['address'] = address1
    df9['beds'] = beds

#create empty url list
urls = []

#loop through url, pull the href and strip out the address tag
for link in soup9.find_all("article"):
    href = link.find('a',class_="list-card-link")
    if href == None:
        addresses = None
    else:
        addresses = href.find('address',class_="list-card-addr").get_text()
    urls.append(addresses)
    urls = [x for x in urls if x is not None]

#import urls into a links column
df9['links'] = urls
df9['links'] = df9['links'].astype('str')

#remove html tags
# df9['links'] = df9['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
# df9['links'] = df9['links'].replace('" tabindex="0"></a>', ' ', regex=True)

df = df.append(df2, ignore_index = True) 
df = df.append(df3, ignore_index = True) 
df = df.append(df4, ignore_index = True) 
df = df.append(df5, ignore_index = True) 
df = df.append(df6, ignore_index = True) 
df = df.append(df7, ignore_index = True) 
df = df.append(df8, ignore_index = True) 
df = df.append(df9, ignore_index = True)

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
df['beds'] = df['beds'].replace('<ul class="list-card-details"><li class="">', ' ', regex=True)
df['beds'] = df['beds'].replace('<ul class="list-card-details"><li>', ' ', regex=True)
df['beds'] = df['beds'].replace('<abbr class="list-card-label"> <!-- -->bds</', ' ', regex=True)
df['beds'] = df['beds'].replace('<abbr class="list-card-label"> <!-- -->bds</abbr></li><li>', ' ', regex=True)
df['beds'] = df['beds'].replace('<abbr class="list-card-label"> <!-- -->ba</abbr></li><li>', ' ', regex=True)
df['beds'] = df['beds'].replace('<abbr class="list-card-label"> <!-- -->bd</abbr></li><li>', ' ', regex=True)
df['beds'] = df['beds'].replace('<abbr class="list-card-label"> <!-- -->sqft</abbr></li></ul>', ' ', regex=True)
df['beds'] = df['beds'].replace(' abbr></li><li class="">', '|', regex=True)
df['beds'] = df['beds'].replace('Studio</li><li>', '0 ', regex=True)
df['beds'] = df['beds'].replace('<abbr class="list-card-label"> <!-- -->ba</', ' ', regex=True)
df['beds'] = df['beds'].replace(' abbr></li><li class="">', '|', regex=True)
df['beds'] = df['beds'].replace('<abbr class="list-card-label"> <!-- -->sqft</abbr></li><li class="list-card-statusText">- House for sale</li></ul>', ' ', regex=True)
df['beds'] = df['beds'].replace('<abbr class="list-card-label"> <!-- -->sqft</abbr></li><li class="list-card-statusText">- Condo for sale</li></ul>', ' ', regex=True)

df.columns = ['prices','address','bed_bath_sqft','links']
#split beds column into beds, bath and sq_feet
# df[['beds','baths','sq_feet']] = df.beds.str.split(expand=True)
# df[['baths']] = df.beds.str.split('|',expand=True)
# df[['sq_feet']] = df.baths.str.split('|',expand=True)

#remove commas from sq_feet and convert to float
df.replace(',','', regex=True, inplace=True)

#drop nulls
df = df[(df['prices'] != '') & (df['prices']!= ' ')]

#convert column to float
df['prices'] = df['prices'].astype('float')
# d['sq_feet'] = df['sq_feet'].astype('float')

#remove spaces from link column
# df['links'] = df.links.str.replace(' ','')

#display
display(df.head())

print('The column datatypes are:')
print(df.dtypes)
print('The dataframe shape is:', df.shape)

#rearrange the columns
# df = df[['prices', 'address', 'links', 'beds', 'baths', 'sq_feet']]

# df

#calculate the zestimate and insert into a dataframe
zillow_zestimate = []
for link in df['links']:
    r = s.get(link, headers=req_headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    home_value = soup.select_one('h4:contains("Home value")')
    if not home_value:
        home_value = soup.select_one('.zestimate').text.split()[-1]
    else:
        home_value = home_value.find_next('p').get_text(strip=True)
    zillow_zestimate.append(home_value)

cols=['zestimate']
zestimate_result = pd.DataFrame(zillow_zestimate, columns=cols)
# zestimate_result

#convert zestimate column to float, and remove , and $
zestimate_result['zestimate'] = zestimate_result['zestimate'].str.replace('$','')
zestimate_result['zestimate'] = zestimate_result['zestimate'].str.replace('/mo','')
zestimate_result['zestimate'] = zestimate_result['zestimate'].str.replace(',','')

#covert rows with non zestimate to 0
def non_zestimate(zestimate_result):
    if len(zestimate_result['zestimate']) > 20:
        return '0'
    elif len(zestimate_result['zestimate']) < 5:
        return '0'
    else:
        return zestimate_result['zestimate']

zestimate_result['zestimate'] = zestimate_result.apply(non_zestimate,axis=1)

# zestimate_result

#concat zestimate dataframe and original df
df = pd.concat([df, zestimate_result], axis=1)
df['zestimate'] = df['zestimate'].astype('float')

#create best deal column and sort by best_deal
df ['best_deal'] = df['prices'] - df['zestimate']
df = df.sort_values(by='best_deal')

df