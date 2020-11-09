# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 23:12:04 2020

@author: islan
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

db_old = pd.read_csv("old_vol.csv")
db = pd.read_csv("car_accident_by_old_age.csv")
old_total = db_old["old_vol"]
all_total = db["All_total"]
sex_total = db["Sex_total"]
year = db["Year"]
male = db["male"]
female = db["female"]
a1_vol = db["A1"]
a2_vol = db["A2"]
big_car = db["大客車"]
sma_car = db["小客車"]
big_tr = db["大貨車"]
sma_tr = db["小貨車"]
big_bi = db["重型機車"]
sma_bi = db["輕型機車"]
bike = db["自行車"]
pop = db["行人"]
other = db["其他"]
old_total = list(old_total)
all_total = list(all_total)
sex_total = list(sex_total)
year = list(year)
male = list(male)
female = list(female)
a1_vol = list(a1_vol)
a2_vol = list(a2_vol)
big_car = list(big_car)
sma_car = list(sma_car)
big_tr = list(big_tr)
sma_tr = list(sma_tr)
big_bi = list(big_bi)
sma_bi = list(sma_bi)
bike = list(bike)
pop = list(pop)
other = list(other)
#資料整理

plt.plot(year, old_total, color='r',label = "Total old pop")
plt.xlabel('Y e a r')
plt.xticks(year, rotation='vertical')
plt.title('Old pop in Taipei') # 設定圖表標題
plt.legend(loc = 'upper left')
plt.show()
#折線圖
plt.plot(year, sex_total, color='r',label="Total old pop by car accident")
plt.xlabel('Y e a r')
plt.xticks(year, rotation='vertical')
plt.title('Car Accident by old age') # 設定圖表標題
plt.legend(loc = 'upper left')
plt.show()
#折線圖


plt.plot(year, male, color='b',label = "Male")
plt.plot(year, female, color='r',label = "Female")
plt.xlabel('Y e a r')
plt.xticks(year, rotation='vertical')
plt.title('Car Accident by Sex') # 設定圖表標題
plt.legend(loc = 'upper left')
plt.show()
#折線圖
plt.plot(year, a1_vol, color='b',label = "A1")
plt.plot(year, a2_vol, color='r',label = "A2")
plt.xlabel('Y e a r')
plt.xticks(year, rotation='vertical')
plt.title('Car Accident by Type') # 設定圖表標題
plt.legend(loc = 'upper left')
plt.show()
#折線圖
plt.plot(year, big_car, color='b',label = "big_car")
plt.plot(year, sma_car, color='r',label = "sma_car")
plt.plot(year, big_tr, color='g',label = "big_tr")
plt.plot(year, sma_tr, color='c',label = "sma_tr")
plt.plot(year, big_bi, color='m',label = "heavy_bi")
plt.plot(year, sma_bi, color='y',label = "light_bi")
plt.plot(year, bike, color='k',label = "bike")
plt.plot(year, pop, color='coral',label = "Human")
plt.plot(year, other, color='grey',label = "Other")
plt.xlabel('Y e a r')
plt.xticks(year, rotation='vertical')
plt.title('Car Accident by Car Type') # 設定圖表標題
plt.legend(loc = 'upper left')
plt.show()
#折線圖
year = np.array(year)
year = np.reshape(year,(len(year),1))
old_total = np.array(old_total)
old_total = np.reshape(old_total,(len(old_total),1))
sex_total = np.array(sex_total)
sex_total = np.reshape(sex_total,(len(sex_total),1))
male = np.array(male)
male = np.reshape(male,(len(male),1))
sma_car = np.array(sma_car)
sma_car = np.reshape(sma_car,(len(sma_car),1))
a2_vol = np.array(a2_vol)
a2_vol = np.reshape(a2_vol,(len(a2_vol),1))

lm = LinearRegression()

lm.fit(male, old_total)
Male_r_squared = lm.score(male, old_total)

lm.fit(sma_car, old_total)
sma_car_r_squared = lm.score(sma_car, old_total)

lm.fit(a2_vol, old_total)
A2_r_squared = lm.score(a2_vol, old_total)

print("Male_r_squared:",Male_r_squared)
print("sma_car_r_squared:",sma_car_r_squared)
print("A2_r_squared:",A2_r_squared)
#回歸分析
print("")

lm.fit(sma_car, male)
sma_car_male_r_squared = lm.score(sma_car, male)

lm.fit(a2_vol, male)
A2_male_r_squared = lm.score(a2_vol, male)

print("sma_car_male_r_squared:",sma_car_male_r_squared)
print("A2_male_r_squared:",A2_male_r_squared)
#回歸分析
male_sma_car_a2 = []
for k in range(len(male)):
    male_sma_car_a2.append([male[k][0], sma_car[k][0],a2_vol[k][0]])

lm.fit(male_sma_car_a2, old_total)
male_sma_car_a2_r_squared = lm.score(male_sma_car_a2, old_total)
#print(lm.coef_)
print("male_sma_car_a2_r_squared:",male_sma_car_a2_r_squared)
#回歸分析
lm.fit(year,old_total)
Male_r_squared = lm.score(year,old_total)
to_be_predicted = np.array([108,109,110])
predicted_accident = lm.predict(np.reshape(to_be_predicted,(len(to_be_predicted),1)))
print(predicted_accident)
#預測

lm.fit(old_total,male)
Male_r_squared = lm.score(old_total,male)
to_be_predicted = np.array([463877,479010,494143])
predicted_accident = lm.predict(np.reshape(to_be_predicted,(len(to_be_predicted),1)))
print(predicted_accident)
#預測