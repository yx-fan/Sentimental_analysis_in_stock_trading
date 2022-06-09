#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 22:12:43 2020

@author: yuxinfan
"""
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib. pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn import neighbors
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

os.chdir("/Users/yuxinfan/471Project")

path = 'dataset.csv'
dataset = pd.read_csv(path)
X = dataset.iloc[:, 11:17]
Y = dataset.iloc[:, 10]

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25, shuffle = False, random_state = 0)

reg = LinearRegression().fit(X_train, y_train)
reg.score(X_test, y_test)
# .00503264936288883

plt.scatter(X_train.iloc[:,5], y_train)

# 0 1 as Y
X = dataset.iloc[:, 11:17]
Y = dataset.iloc[:, 17]

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25, shuffle = False, random_state = 0)

regrscore = []
for i in range(1, 30):
    regr = DecisionTreeClassifier(max_depth=i)
    regr.fit(X_train, y_train)
    regrscore.append(regr.score(X_test, y_test))
plt.scatter(list(range(1,30)), regrscore)
# depth = 7 maximum

scaler = StandardScaler()
new_X = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(new_X, Y, test_size = 0.25, shuffle = False, random_state = 0)

knnscore = []
for K in range(1, 30):
    knn = neighbors.KNeighborsRegressor(n_neighbors= K)
    knn.fit(X_train, y_train)
    knnscore.append(knn.score(X_test, y_test))
plt.scatter(list(range(1,30)), knnscore)
# knn is not a good method

clf = LogisticRegression(random_state=0).fit(X_train, y_train)
clf.score(X_test, y_test)
# 0.6358024691358025
