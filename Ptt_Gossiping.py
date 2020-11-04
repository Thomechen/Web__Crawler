import requests
from bs4 import BeautifulSoup
import re
session = requests.Session()

my_data = {"from": "/bbs/Gossiping/index.html",
           "yes": "yes"}

r = session.post('https://www.ptt.cc/ask/over18',data=my_data)

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

search = input('輸入關鍵字查詢:')
if search == "":
    search = ""

page = input('輸入欲搜尋頁數(預設:1):')
if page == "":
    page = 1
    
dates = input('輸入日期(MM/DD):')
if dates =="":
    dates =""

a = 1

while a <= int(page):
    r2 = session.get(url)
    if r2.status_code == 200:
        soup = BeautifulSoup(r2.text,'html.parser')
        titles = soup.select('div.title')
        links = soup.select('div.title > a')
        date = soup.select('div.date')
        newUrl = 'https://www.ptt.cc'+soup.select('div.btn-group.btn-group-paging > a')[1].get('href')
        for t,l,d in zip(titles,links,date):
            if 'Re:' in t.text or 'Fw:' in t.text or search not in t.text or dates not in d.text:
                 continue
            print(d.text+' 標題:'+t.text.strip())
            r3 = session.get('https://www.ptt.cc'+l.get('href'))
            soup2 = BeautifulSoup(r3.text,'html.parser')
            content = soup2.select_one('div#main-content').text
            target_content = u'※ 發信站: 批踢踢實業坊(ptt.cc),'
            content = content.split(target_content)[0]
            
            date = soup2.select('span.article-meta-value')[3].text
            content = content.split(date)[1]
            # print(content)
        url = newUrl
        a += 1