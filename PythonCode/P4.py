#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 12:33:30 2020

@author: yuxinfan
"""

import os
import glob
from string import punctuation
import re
import pandas as pd

os.chdir("/Users/yuxinfan/471Project/worddic")
df=pd.read_csv('stop_2020.csv')
stoplist = df.copy()
stoplist = list(stoplist['ABOUT'])

os.getcwd()
os.chdir("/Users/yuxinfan/471Project/10-K")

filepath_list = []
for filename in glob.glob("*.txt"):
    filepath_list.append(''.join(filename))
    
# preprocessing    
for file in filepath_list:
    print(file)
    file_content = open(file)
    file_list = file_content.read()
    file_process = file_list.upper()

    for p in ["\n", "\t", "\a", "\b", "\r", "\v", "\xa0", "—"]:
        file_process = file_process.replace(p,' ')
        
    for p in list(punctuation):
        file_process = file_process.replace(p,' ')
        
    file_process = file_process.replace('”', ' ').replace('“', ' ').replace('————', ' ').replace('———', ' ').replace('——', ' ').replace('-', ' ')
    file_process = file_process.replace('   ',' ').replace('  ',' ')

    word_each = file_process.split()
    word_each = [x for x in word_each if not (x.isdigit() 
                                         or x[0] == '-' and x[1:].isdigit())]

    for num in (1, 100):
        for word in word_each:
            if re.search('[0-9]', word):
                word_each.remove(word)

    word_each = [i for i in word_each if len(i) > 1]

    text_file = open('Wordbag%s'%file, "w")
    n = text_file.write(str(word_each))
    file_content.close()
    text_file.close()

