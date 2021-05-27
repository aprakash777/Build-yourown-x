# -*- coding: utf-8 -*-
"""
Created on Sat May 22 23:31:21 2021

@author: Akshay Prakash
"""

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
x = np.array([1,2,3,4,5,6,7]).reshape(-1,1)
y = np.array([9,8,10,12,11,13,14])
print(x, y)
print(x.shape, y.shape) #(rows, columns)
model = LinearRegression().fit(x,y)#Creates the best linear reggression line for the variable data
r_sqrt = model.score(x,y) #r_sqrt is the co-eff of Determination
print('r_sqrt: ', r_sqrt)
intercept = model.intercept_
slope = model.coef_
print('intercept: ', intercept)
print('slope: ', slope)
y_predicted = model.predict(x)
print('y_predicted: ', y_predicted)
y_new = intercept + slope * x
fig, ax = plt.subplots(figsize =(10,10))
plt.scatter(x, y)
plt.plot(x, y_new)
