#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 19:11:43 2020

@author: yuxinfan
"""

import os
import pandas as pd
import numpy as np

os.chdir("/Users/yuxinfan/471Project")

path = 'WORD_COUNT.csv'
df = pd.read_csv(path)

path1 = 'MONTHLY_RET.csv'
df1 = pd.read_csv(path1)

path2 = 'CIK_MAP_FINAL.csv'
CIK_MAP = pd.read_csv(path2)

df1['Month'] = pd.DatetimeIndex(df1['date']).month
df1['Day'] = pd.DatetimeIndex(df1['date']).day

df['Ret'] = 0

Database = df1.merge(CIK_MAP, left_on = 'cusip', right_on = 'CUSIP')


count = 0
for num1 in range(0, len(df['CIK'])):
    for num2 in range(0, len(Database['CIK'])):
        if df.iloc[num1, 0] == Database.iloc[num2, 25]:
            if df.iloc[num1, 3] == 12:
                if df.iloc[num1, 2] + 1 == Database.iloc[num2, 22] and Database.iloc[num2, 23] == 1:
                    df.iloc[num1, 9] = Database.iloc[num2, 12]
                    print(Database.iloc[num2, 12])
                    count += 1
            else:
                if df.iloc[num1, 2] == Database.iloc[num2, 22] and df.iloc[num1, 3] + 1 == Database.iloc[num2, 23]:
                    df.iloc[num1, 9] = Database.iloc[num2, 12]
                    print(Database.iloc[num2, 12])
                    count += 1
                    
dataset = df[df['Ret'] != 0]
dataset['POS_PER'] = dataset['POS_NUM']/dataset['TOL_NUM']
dataset['NEG_PER'] = dataset['NEG_NUM']/dataset['TOL_NUM']
dataset['UNCERTAIN_PER'] = dataset['UNCERTAIN_NUM']/dataset['TOL_NUM']
dataset['LOG_POS'] = np.log10(dataset['POS_NUM'])
dataset['LOG_NEG'] = np.log10(dataset['NEG_NUM'])
dataset['LOG_UN'] = np.log10(dataset['UNCERTAIN_NUM'])
signlist = []
for item in dataset['Ret']:
    if item > 0:
        sign = 1
    else: sign = 0
    signlist.append(sign)
dataset['signlist'] = signlist

os.chdir("/Users/yuxinfan/471Project")
dataset.to_csv('dataset.csv')



