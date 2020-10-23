# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 00:09:09 2020

@author: islan
"""

import requests
from bs4 import BeautifulSoup
sinput = eval(input('想要看幾頁的標題:'))
i = 0
for i in range(sinput+1):
    if i == 1:
        r = requests.get('https://forum.gamer.com.tw/B.php?bsn=60433')
        soup = BeautifulSoup(r.text,'html.parser')
        titles = soup.find_all('p',class_="b-list__main__title")
        for t in titles:
            print(t.string)
            print("https://forum.gamer.com.tw/"+t.get('href'))
    elif i > 1:
        r = requests.get('https://forum.gamer.com.tw/B.php?page={}&bsn=60433'.format(str(i)))
        soup = BeautifulSoup(r.text,'html.parser')
        titles = soup.find_all('p',class_="b-list__main__title")
        for t in titles:
            print(t.string)
            print("https://forum.gamer.com.tw/"+t.get('href'))
i += 1

