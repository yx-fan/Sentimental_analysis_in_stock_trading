#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 21:04:25 2020

@author: yuxinfan
"""

import os
import glob
import re

os.chdir("/Users/yuxinfan/471Project/worddic")
                
pos_sent = open("positive_2020.csv")
positive_words=pos_sent.read().lower().split('\n')
positive_words.remove('')
pos_sent.close()

neg_sent = open('negative_2020.csv')
negative_words=neg_sent.read().lower().split('\n')
negative_words.remove('')
neg_sent.close()

uncertain_sent = open('uncertainty_2020.csv')
uncertain_words=uncertain_sent.read().lower().split('\n')
uncertain_words.remove('')
uncertain_sent.close()



os.chdir("/Users/yuxinfan/471Project/Wordbag")

filepath_list = []
for filename in glob.glob("*.txt"):
    filepath_list.append(''.join(filename))
    
    
CIK = []
Date = []
positive_num = []
negative_num = []
total_num = []
uncertain_num = []
for file in filepath_list:
    print(file)
    CIKnum = re.findall('WordbagReport10K([0-9].*)\|', file)
    Datenum = re.findall('Word.*\|([0-9].*)\.txt', file)
    CIK.append(CIKnum)
    Date.append(Datenum)
    
    # Open annual report and preprocessing
    file_content = open(file)
    word_list = file_content.read()
    word_list = word_list.replace("'", '').replace('[', '').replace(']', '').replace(',', '').replace('GAAP', '')
    word_list = word_list.split()
    for num in (1, 200):
        for word in word_list:
            if re.search('[0-9]', word):
                word_list.remove(word)
    file_content.close()
    
    word_count = len(word_list)
    positive_counter = 0    
    negative_counter = 0
    uncertain_counter = 0
    for word in word_list:    
        word_processed = word.lower()
        
        if word in positive_words:
            positive_counter = positive_counter + 1
    
        if word in negative_words:
            negative_counter = negative_counter + 1           

        if word in uncertain_words:
            uncertain_counter = uncertain_counter + 1
            
    positive_num.append(positive_counter)    
    negative_num.append(negative_counter)   
    uncertain_num.append(uncertain_counter)
    total_num.append(word_count)

re.findall('Word.*\|([0-9].*)\.txt', 'WordbagReport10K64803|2018214.txt')

















