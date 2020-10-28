import requests
from bs4 import BeautifulSoup
import re
my_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.51'}
url = 'https://www.inside.com.tw/'
r = requests.get(url)
tags = ['5G','AI']
categroys = ['startup','opinion','區塊鏈','dictionary']
features = ['aws-tldg-2020','2019aws']
a_l_tag = []
l_l_tag = []
a_l_categroy =[]
l_l_categroy =[]
if r.status_code == 200:
    # print('網頁讀取成功')
    for i in range(len(tags)):
        r = requests.get(url+'tag/'+tags[i],headers=my_headers)
        soup = BeautifulSoup(r.text,'html.parser')
        titles = soup.find_all('a',class_='js-auto_break_title',limit=10)
        links = soup.find_all('a',class_='post_cover',limit=10)
        for t,l in zip(titles,links):
            a_l_tag.append(t.text)
            l_l_tag.append(l.get('href'))
            
    for j in range(len(categroys)):
        r = requests.get(url+'category/'+categroys[j],headers=my_headers)
        soup = BeautifulSoup(r.text,'html.parser')
        titles = soup.find_all('a',class_='js-auto_break_title',limit=10)
        links = soup.find_all('a',class_='post_cover',limit=10)
        for t,l in zip(titles,links):
            a_l_categroy.append(t.text)
            l_l_categroy.append(l.get('href'))
else:
    print('請加上headers')
