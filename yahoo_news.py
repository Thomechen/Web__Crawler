# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 13:54:04 2020

@author: islan
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
request = requests.Session()
url = 'https://tw.news.yahoo.com/'
r = request.get(url)
title_list = []
#
links_list = []
if r.status_code == 200:
    soup = BeautifulSoup(r.text,'html.parser')
    titles = soup.find_all('li',class_='Pos(r) Lh(1.5) H(24px) Mb(8px)')
    #頭條標題
    links = soup.find_all('a',class_='D(ib) Ov(h) Whs(nw) C($c-fuji-grey-l) C($c-fuji-blue-1-c):h Td(n) Fz(16px) Tov(e) Fw(700)')
    #標題連結
    for t,l in zip(titles,links) :
        print(t.text)
        title_list.append(t.text)
        print(l.get('href'))
        links_list.append(l.get('href'))
data = {'story_title':title_list,'links':links_list}
df = pd.DataFrame(data)
#資料框架建立