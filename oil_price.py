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
# date = r['調價日期']
oil_92 = r["92 無鉛汽油"]
oil_95 = r["95 無鉛汽油"]
oil_98 = r["98 無鉛汽油"]
oil_super = r["超級/高級柴油"]
oil_price_list = [oil_92,oil_95,oil_98,oil_super]
oil_tag_list = ["Oil_92","Oil_95","Oil_98","Oil_super"]
#92/95/98/超柴歷史紀錄圖表建立
for o_p_l,o_t_l in zip(oil_price_list,oil_tag_list):
    plt.plot(r.index, o_p_l, color='r',label = o_t_l)
    plt.xlabel('Date')
    plt.xticks(r.index, rotation='vertical')
    plt.title(o_t_l+' price history') # 設定圖表標題
    plt.legend(loc = 'upper left')
    plt.show()
