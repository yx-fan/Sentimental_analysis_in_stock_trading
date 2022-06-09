#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 20:36:37 2020

@author: yuxinfan
"""

import pandas as pd
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup

os.getcwd()
os.chdir("/Users/yuxinfan/471Project")

# input List10K file generated from last step
path='List10K.csv'
df=pd.read_csv(path)
dataset_10K = df.copy()

dataset_10K['month'] = pd.DatetimeIndex(dataset_10K['Datelist']).month
dataset_10K['day'] = pd.DatetimeIndex(dataset_10K['Datelist']).day

# Webcrawling and store
os.chdir("/Users/yuxinfan/471Project/10-K")
for num in range(0,len(dataset_10K['Htmllist'])):
    print(num)
    one10K = list(dataset_10K.iloc[num,:])
    url = one10K[5]
    CIK = one10K[0]
    Year = one10K[4]
    Month = one10K[6]
    Day = one10K[7]
    # Open url
    pageOpen = urlopen(url)
    soup = BeautifulSoup(pageOpen, "html.parser")
    text = soup.get_text(strip = True)
    # Output text
    textname = "Report10K" + str(CIK) + "|" + str(Year) + str(Month) + str(Day) + ".txt"
    text_file = open(textname, "w")
    n = text_file.write(text)
    # Close
    text_file.close()
    pageOpen.close()

