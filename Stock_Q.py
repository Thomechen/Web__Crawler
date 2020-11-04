# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 21:03:03 2020

@author: ASUS
"""


import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
request = requests.Session()

year = ['2017','2018','2019']

url = 'http://www.stockq.org/stock/history/'

for y in range(len(year)):
    url_1 = url + year[y] +"/"
    for m in range(1,13,1):
        if m - 10 < 0:
            m = '0' + str(m) 
            url_2 = url_1 + str(m) +'/'
        else:
            m = str(m) 
            url_2 = url_1 + str(m) +'/'
        for d in range(1,32,1):
            try:
                if d - 10 < 0:
                    d = '0' + str(d)
                    url_3 = url_2 + year[y] + str(m) +str(d) +'_tc.php'
                    r = request.get(url_3)
                    soup = BeautifulSoup(r.text,'html.parser')
                    value = soup.select('tr.row2')[3]
                    print(value.text)
                    print(year[y] + str(m) +str(d))
                else:
                    d = str(d)
                    url_3 = url_2 + year[y] + str(m) + str(d) +'_tc.php'
                    r = request.get(url_3)
                    soup = BeautifulSoup(r.text,'html.parser')
                    value = soup.select('tr.row2')[3]
                    print(value.text)
                    print(year[y] + str(m) +str(d))
            except:
                continue
    
# soup = BeautifulSoup(r.text,'html.parser')
# value = soup.select('tr.row2')[3]
# print(value.text)