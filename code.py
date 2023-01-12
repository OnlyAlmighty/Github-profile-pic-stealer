import requests
from bs4 import BeautifulSoup as bs
import time,os

username = input("Enter The username : ")
time.sleep(5)
print(1)
time.sleep(1)
print(2)
time.sleep(1)
print(3)
time.sleep(1)
print(4)
time.sleep(1)
print(5)
time.sleep(1)
print("here is your output")
url = 'https://github.com/'+username
r = requests.get(url)
soup = bs(r.content,'html.parser')
profile_img = soup.find('img',{'alt': 'Avatar'})['src']
print(profile_img)
