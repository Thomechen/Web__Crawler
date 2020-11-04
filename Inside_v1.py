import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
my_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.51'}
url = 'https://www.inside.com.tw/'
r = requests.get(url)
url_list = ['tag/','category/','feature/']
tags = ['5G','AI']
categorys = ['startup','opinion','區塊鏈','dictionary']
features = ['aws-tldg-2020','2019aws']
url_tag_list = []
url_categorys_list = []
url_features_list = []


for i in range(len(url_list)):
    if i == 0:
        for j in range(len(tags)):        
            url_tags = (url+url_list[0]+tags[j])
            url_tag_list.append(url_tags)
    elif i == 1:
        for j in range(len(categorys)):
            url_categorys = (url+url_list[1]+categorys[j])
            url_categorys_list.append(url_categorys)
    elif i == 2:
        for j in range(len(features)):
            url_features = (url+url_list[2]+features[j])
            url_features_list.append(url_features)
            
# for i in range(len(tags)):
#     r = requests.get(url+'tag/'+tags[i],headers=my_headers)
#     soup = BeautifulSoup(r.text,'html.parser')
#     titles = soup.find_all('a',class_='js-auto_break_title')
#     links = soup.find_all('a',class_='post_cover')
#     if i == 0:
#         for t,l in zip(titles,links):
#             FiveG_list.append(t.text)
#             FiveG_link.append(l.get('href'))
#     elif i == 1:
#         for t,l in zip(titles,links):
#             AI_list.append(t.text)
#             AI_link.append(l.get('href'))
            
# Tag_data = {'5G Article list':FiveG_list,'5G_Link':FiveG_link,
#             'AI Article list':AI_list,'AI_Link':AI_link}
# Tag = pd.DataFrame(Tag_data)


