#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 12:00:18 2020

@author: yuxinfan
"""

import wrds
import pandas as pd
import os

os.getcwd()
os.chdir("/Users/yuxinfan/471Project")

conn = wrds.Connection()
conn.list_libraries()

msf = conn.get_table(library = 'crsp', table = 'msf')
msf.head(5)
msf.dtypes
msf['Year'] = pd.DatetimeIndex(msf['date']).year
df1 = msf[msf['Year'] >= 2016]

path = 'CIK_MAP_FINAL.csv'
CIK_MAP = pd.read_csv(path)
len(df1['cusip'].unique())
count = 0
for item in CIK_MAP['CUSIP']:
    if item in df1['cusip'].unique():
        count += 1
# count is 312
# cusip list we have is 377

df2 = df1[df1['cusip'].isin(list(CIK_MAP['CUSIP']))]

df2.to_csv('MONTHLY_RET.csv')
