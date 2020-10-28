import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
my_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.51'}
url = 'https://www.inside.com.tw/'
r = requests.get(url)
tags = ['5G','AI']
categroys = ['startup','opinion','區塊鏈','dictionary']
categroys_name = ['新創','評論','區塊鏈','硬塞科技字典']
features = ['aws-tldg-2020','2019aws']
features_name = ['數位轉型思維','雲端趨勢服務']
a_l_tag = []
l_l_tag = []
a_l_categroy =[]
l_l_categroy =[]
a_l_features =[]
l_l_features =[]
if r.status_code == 200:
    # print('網頁讀取成功')
    for i in range(len(tags)):
        r = requests.get(url+'tag/'+tags[i],headers=my_headers)
        soup = BeautifulSoup(r.text,'html.parser')
        titles = soup.find_all('a',class_='js-auto_break_title')
        links = soup.find_all('a',class_='post_cover')
        for t,l in zip(titles,links):
            a_l_tag.append(t.text)
            l_l_tag.append(l.get('href'))
            
    for j in range(len(categroys)):
        r = requests.get(url+'category/'+categroys[j],headers=my_headers)
        soup = BeautifulSoup(r.text,'html.parser')
        titles = soup.find_all('a',class_='js-auto_break_title')
        links = soup.find_all('a',class_='post_cover')
        a_l_categroy.append(categroys_name[j]+'-----------------')
        for t,l in zip(titles,links):
            a_l_categroy.append(t.text)
            l_l_categroy.append(l.get('href'))
            
    for k in range(len(features)):
        r = requests.get(url+'feature/'+features[k],headers=my_headers)
        soup = BeautifulSoup(r.text,'html.parser')
        titles = soup.find_all('a',class_='js-auto_break_title')
        links = soup.find_all('a',class_='post_cover')
        a_l_features.append(features_name[k]+'-----------------')
        for t,l in zip(titles,links):
            a_l_features.append(t.text)
            l_l_features.append(l.get('href'))
else:
    print('請加上headers')
    
article_data = {'a_l_tag':a_l_tag,'l_l_tag':l_l_tag}
d = pd.DataFrame(article_data)
