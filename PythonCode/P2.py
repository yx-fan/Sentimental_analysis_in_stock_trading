#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 17:53:16 2020

@author: yuxinfan
"""

import pandas as pd
import os

os.getcwd()
os.chdir("/Users/yuxinfan/471Project")

# input our htmlindex file generated from last step
path='htmlindex.csv'
df=pd.read_csv(path)
dataset = df.copy()
dataset = dataset.dropna(subset=['Datelist'])
dataset['year'] = pd.DatetimeIndex(dataset['Datelist']).year
dataset['month'] = pd.DatetimeIndex(dataset['Datelist']).month
dataset['day'] = pd.DatetimeIndex(dataset['Datelist']).day
dataset = dataset[dataset.year != 2016]
dataset = dataset[dataset.year != 2017]

# Generate 10-K url 
dataset_10K = dataset[dataset['Typelist'] == '10-K']
urllist = []

for num in range(0,len(dataset_10K['Htmllist'])):
    print(num)
    index = list(dataset_10K['Htmllist'])[num]
    CIK = list(dataset_10K['CIKlist'])[num]
    Filing = index.split("|")
    for item in Filing:
        if 'html' in item:
            report = item
            url = 'https://www.sec.gov/Archives/' + report
            df1 = pd.read_html(url)
            document_index = df1[0]
            document_index = document_index.dropna(subset=['Type'])
            document_name = document_index[document_index['Type'].str.contains('10-K')]
            document_name = document_name['Document'].str.split(' ')
            document_name = document_name[0][0]
            report_formatted = report.replace('-','').replace('index.html','')
            url = 'https://www.sec.gov/Archives/' + report_formatted + '/' + document_name
            urllist.append(url)

dataset_10K['urllist'] = urllist



        

        
        
        
        
        
        
        
        
        
        
        
        
