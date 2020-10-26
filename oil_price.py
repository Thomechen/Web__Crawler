# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 14:26:55 2020

@author: islan
"""
import pandas as pd
import numpy as np
r = pd.read_excel("oil_price.xlsx",sheet_mame="oil_price")
date = r["調價日期"]
oil_92 = r["92 無鉛汽油"]
oil_95 = r["95 無鉛汽油"]
oil_98 = r["98 無鉛汽油"]
oil_super = r["超級/高級柴油"]
