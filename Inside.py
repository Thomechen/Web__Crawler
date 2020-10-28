import requests
from bs4 import BeautifulSoup
import re
url = 'https://www.inside.com.tw/'
r = requests.get(url)
if r.status_code == 200:
    print('網頁讀取成功')
    test = r.text
else:
    print('請加上headers')
