from wsgiref import headers
from fastapi import Query
import requests
from bs4 import BeautifulSoup
from re import search


headers = { "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.50}" }


tempGovSite = input('Please enter Philippine government website: ')
print("")
print("Now Scanning: https://www." +tempGovSite)
print("")

print("---------EXPOSED DATA FILES----------")
print("")
query = "https://www.google.com/search?q=site%3A"+tempGovSite+"+inurl%3Aadmin+filetype%3Apdf"         
req = requests.get(query, headers=headers)

soup = BeautifulSoup(req.text, "html.parser")
divs = soup.find('div', id="rso")
if divs is None:
    print("No contents found.")
else:
    a_tags = divs.find_all('div', class_='yuRUbf')
    for div in a_tags:
        a = div.find('a',href=True)
        print(a.attrs['href'])
    print("")
        
print("")
print("----------EXPOSED DATA LINKS----------")
print("")
query = "https://www.google.com/search?q=site%3A"+tempGovSite+"+inurl%3Aadmin+intext%3Aindex+of+%2F"         
req = requests.get(query, headers=headers)

soup = BeautifulSoup(req.text, "html.parser")
divs = soup.find('div', id="rso")
if divs is None:
    print("No contents found.")
    
else:
    a_tags = divs.find_all('div', class_='yuRUbf')
    for div in a_tags:
        a = div.find('a',href=True)
        print(a.attrs['href'])
    print("")









