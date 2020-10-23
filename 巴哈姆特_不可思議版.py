# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 00:09:09 2020

@author: islan
"""

import requests
from bs4 import BeautifulSoup
url = 'https://forum.gamer.com.tw/B.php?bsn=60433'
r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')
titles = soup.find_all('p',class_="b-list__main__title")

for t in titles:
    print(t.string)
    print("https://forum.gamer.com.tw/"+t.get('href'))
    


