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
        for t,l in zip(titles,links):
            a_l_categroy.append(t.text)
            l_l_categroy.append(l.get('href'))
            
    for k in range(len(features)):
        r = requests.get(url+'feature/'+features[k],headers=my_headers)
        soup = BeautifulSoup(r.text,'html.parser')
        titles = soup.find_all('a',class_='js-auto_break_title')
        links = soup.find_all('a',class_='post_cover')
        for t,l in zip(titles,links):
            a_l_features.append(t.text)
            l_l_features.append(l.get('href'))

a_l_tag_data = {'Tag_article':a_l_tag,'Tag_Link':l_l_tag}
Tag_d = pd.DataFrame(a_l_tag_data)
a_l_categroy_data = {'Categroy_article':a_l_categroy,'Categroy_Link':l_l_categroy}
Categroy_d = pd.DataFrame(a_l_categroy_data)
a_l_features_data = {'Features_article':a_l_features,'Features_Link':l_l_features}
Feature_d = pd.DataFrame(a_l_features_data)

