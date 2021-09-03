import requests

URL = ""
page = requests.get(URL)

print(page.text);