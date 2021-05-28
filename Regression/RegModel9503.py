# -*- coding: utf-8 -*-
"""
Created on Sun May 23 23:40:58 2021

@author: Akshay Prakash
"""
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 
from Regression import result
print(result['Pts'])
y = result.Rk
x = result.Pts.values.reshape(-1,1)
print(x.shape, y.shape)

model = LinearRegression().fit(x, y)
r_sqrt = model.score(x,y)
print("r_sqrt: ", r_sqrt)
intercept = model.intercept_
slope = model.coef_
print('intercept: ', intercept)
print('slope: ', slope)

y_predicted = intercept + slope* x #Linear Regression eqn


y_new = model.predict(x).reshape(-1,1)
print(y_new)


fig, ax = plt.subplots(figsize = (10,10))
plt.scatter(x,y, color = 'blue', label = 'Points')
plt.plot(x,y_predicted, color = 'red', label = 'Linear Regression')
plt.legend()
plt.ylim(0.5, 20.5) #dont do 0 because there's no 0 position
plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]) 
plt.gca().invert_yaxis()#rewrite because it should be from low to high
plt.xlabel('Points')
plt.ylabel('League Position')
plt.title('Evaluating relationship between Points and league position')

plt.text(18, 2.7, "Model based on Points from 95/96- 02/03", color = 'brown', size = '15')
plt.text(16, 4, f'Slope: {slope}', color = 'red', size= '13')
plt.text(16, 4.7, f'Intercept: {intercept}', color = 'red', size= '13')
plt.text(16, 5.4, f'r_sqrt: {r_sqrt}', color = 'red', size= '13')


plt.text(87, 1.4, "Man Utd (91)", color ='red', size = '8')
plt.text(16, 19.6, "Sunderland (19) ", color = 'red', size= '7')

df9 = pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\F0304PL.csv')
print(df9)

y = int(input("Enter a number: "))
x = (y- intercept)/slope
print(x)
