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
pages = str(input("要幾頁的資料:"))
#搜尋關鍵字
url = 'https://www.google.com.tw/search?q='+search
vol = '&ei=A0ShX5m2BYuImAWHyJiAAQ&start='
title_list = []
link_list = []
for i in range(0,int(pages)*10,10):
    r = request.get(url+vol+str(i)) 
    if r.status_code == 200:
        soup = BeautifulSoup(r.text,'html.parser')
        titles = soup.select('div.BNeawe.vvjwJb.AP7Wnd')
        #搜尋標題
        links = soup.select('div.kCrYT > a')
        #標題連結
        for t,l in zip(titles,links):
            print('標題:'+t.text)
            title_list.append(t.text)
            links_l = l.get('href')
            target_links_l = u'/url?q='
            links_l = links_l.split(target_links_l)[1]
            #清除非連結文字
            link_list.append(links_l)
            print('網址:'+links_l)

data = {'Search Title':title_list,'Link':link_list}
df = pd.DataFrame(data)
        
        
        

