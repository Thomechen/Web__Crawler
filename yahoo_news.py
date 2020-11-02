# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 13:54:04 2020

@author: islan
"""

import requests
from bs4 import BeautifulSoup
import re
request = requests.Session()
url = 'https://tw.news.yahoo.com/'
categroy = ['entertainment']
r = request.get(url)
if r.status_code == 200:
    r = request.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    titles = soup.find_all('li',class_='Pos(r) Lh(1.5) H(24px) Mb(8px)')
    for t in titles :
        print(t.text)