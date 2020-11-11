
import re
import time
import pandas
from bs4 import BeautifulSoup
from selenium import webdriver #載入 webdriver 模組

browser = webdriver.Edge("F:\Python\Web__Crawler\msedgedriver.exe")#用edge模擬
browser.get("https://www.cpc.com.tw/historyprice.aspx?n=2890")
time.sleep(2)#休息
source = browser.page_source
browser.quit()
soup = BeautifulSoup(source,'html.parser')
#擷取網頁資訊
change_date_list = []
oil_92_value = []
oil_95_value = []
oil_98_value = []
oil_super_value = []
#建立各項油價清單
change_date = soup('td',{'data-title':'調價日期'})
oil_92 = soup('td',{'data-title':'92 無鉛汽油'})
oil_95 = soup('td',{'data-title':'95 無鉛汽油'})
oil_98 = soup('td',{'data-title':'98 無鉛汽油'})
oil_super = soup('td',{'data-title':'超級/高級柴油'})
#擷取各項油價
for c_d in change_date:
    change_date_list.append(c_d.text)
for o_92 in oil_92:
    oil_92_value.append(o_92.text)
for o_95 in oil_95:
    oil_95_value.append(o_95.text)
for o_98 in oil_98:
    oil_98_value.append(o_98.text)
for o_super in oil_super:
    oil_super_value.append(o_super.text)

data = {'Date':change_date_list,
        'Oil_92':oil_92_value,
        'Oil_95':oil_95_value,
        'Oil_98':oil_98_value,
        'Oil_Super':oil_super_value}

df = pandas.DataFrame(data)



