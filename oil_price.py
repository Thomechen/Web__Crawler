# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 14:26:55 2020

@author: islan
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

r = pd.read_excel("oil_price.xlsx",sheet_mame="oil_price",index_col="調價日期")
r = r.sort_index()
date = r['調價日期']
oil_92 = r["92 無鉛汽油"]
oil_95 = r["95 無鉛汽油"]
oil_98 = r["98 無鉛汽油"]
oil_super = r["超級/高級柴油"]

plt.plot(date, oil_92, color='r',label = "Oil_92")
plt.xlabel('Date')
plt.xticks(date, rotation='vertical')
plt.title('Oil_92 price history') # 設定圖表標題
plt.legend(loc = 'upper left')
plt.show()