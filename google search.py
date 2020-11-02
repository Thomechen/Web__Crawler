# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 15:07:26 2020

@author: islan
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
request = requests.Session()
search = str(input("請輸入欲搜尋關鍵字:"))
#搜尋關鍵字
url = 'https://www.google.com.tw/search?q='
r = request.get(url+search)
title_list = []
link_list = []
if r.status_code == 200:
    soup = BeautifulSoup(r.text,'html.parser')
    titles = soup.select('div.BNeawe.vvjwJb.AP7Wnd')
    #搜尋標題
    links = soup.select('div.kCrYT > a')
    #標題連結
    for t,l in zip(titles,links):
        print(t.text)
        title_list.append(t.text)
        links_l = l.get('href')
        target_links_l = u'/url?q='
        links_l = links_l.split(target_links_l)[1]
        #清除非連結文字
        link_list.append(links_l)
        print(links_l)

data = {'Search Title':title_list,'Link':link_list}
df = pd.DataFrame(data)
        
        
        

