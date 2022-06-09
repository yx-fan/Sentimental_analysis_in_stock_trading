#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 12:25:30 2020

@author: yuxinfan
"""

import os
import pandas as pd
import numpy as np
import csv

os.getcwd()
os.chdir("/Users/yuxinfan/471Project")

# Import the 10-K list that we used for textual analysis
path = 'List10K.csv'
df=pd.read_csv(path)
CIKlist = df['CIKlist'].unique()

# Import the mapping file that we have
path1 = 'CIK_CUSIP.csv'
df1=pd.read_csv(path1)

# Mapping process
CIK = []
CUSIP = []
length = len(df1['CIK'])
year = []
for item in CIKlist:
    print(item)
    for num in range(0, length):
        if item == df1.iloc[num, 1]:
            CIK.append(item)
            CUSIP.append(df1.iloc[num, 3])
            year.append(df1.iloc[num, 0])

CIK_MAP = pd.DataFrame()
CIK_MAP['CIK'] = CIK
CIK_MAP['CUSIP'] = CUSIP
CIK_MAP['YEAR'] = year

# Output the mapping file
output = np.column_stack((CIK, CUSIP, year))
writer=csv.writer(open('output.csv','w', newline=''))
fields = ['CIK', 'CUSIP', 'YEAR'] 
writer.writerow(fields)
writer.writerows(output)

# We output the mapping file since one CIK could have several records of CUSIP
# We order the output file by CIK and year in excel and input again

CIK = []
CUSIP = []
year = []
path2 = 'CIK_MAP.csv'
df2=pd.read_csv(path2)
for item in df2['CIK'].unique():
    table = df2[df2['CIK'] == item]
    CIK.append(table.iloc[0,0])
    CUSIP.append(table.iloc[0,1])
    year.append(table.iloc[0,2])

# Output the final mapping file
output = np.column_stack((CIK, CUSIP, year))
writer=csv.writer(open('CIK_MAP_FINAL.csv','w', newline=''))
fields = ['CIK', 'CUSIP', 'YEAR'] 
writer.writerow(fields)
writer.writerows(output)

