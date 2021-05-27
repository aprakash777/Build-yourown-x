# -*- coding: utf-8 -*-
"""
Created on Sun May 23 02:08:50 2021

@author: Akshay Prakash
"""

import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
df = pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\96-20PL.csv')
df1 = pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\F2021PL.csv')
newframe = [df, df1]
NewResult = pd.concat(newframe)

print(df['Pts'])
y = df.Rk
x = df.Pts.values.reshape(-1,1) #.values with reshape because its DF 
print(x.shape, y.shape) #(rows,colums)
model = LinearRegression().fit(x, y)
r_sqrt = model.score(x,y)
print('r_sqrt: ', r_sqrt)
intercept = model.intercept_
slope = model.coef_
print('intercept: ', intercept)
print('slope: ', slope)
y_predicted = intercept + slope* x #Linear Regression eqn


fig, ax = plt.subplots(figsize = (10,10))
plt.scatter(x,y, color = 'blue', label = 'Points')
plt.plot(x,y_predicted, color = 'red', label = 'Linear Regression')
plt.legend()
plt.ylim(0.5, 20.5) #dont do 0 because there's no 0 position
plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]) 
plt.gca().invert_yaxis()#rewrite because it should be from low to high
plt.xlabel('Points')
plt.ylabel('League Position (Rank)')
plt.title('Evaluating relationship between Points and league position')
plt.text(10, 3, "Slope: -0.332 ", color = 'red', size= '15')
plt.text(10, 3.7, "Intercept: 27.80 ", color = 'red', size= '15')
plt.text(10, 4.4, "r_sqrt: 0.89 ", color = 'red', size= '15')
plt.text(92, 1.4, "Man City 18/19 (98)", color ='red', size = '7')
plt.text(92, 2.4, "Liverpool 18/19 (97)", color ='red', size = '7')
plt.text(7, 19.6, "Derby County 2008/09 ", color = 'red', size= '7')


y = int(input("Enter a number: "))
x = (y- intercept)/slope
print(x)

"""
For example, when a team reaches 81 points (Substitute y= 1 in the y= mx + c eqn) 
they are title contenders for the season. 
They are statistically competing for the title. Of course, it depends on 
when they reach that point. The earlier they reach it, statiscally they are 
running away with the title. Although, there may be exceptional cases such as 
in 18/19 Man city reached the 83 point mark with 5 games left in the season.
They were not confirmed as winners as Liverpool was closing the gap as seen in the plot. 

This season Man City were only confirmed as champions once they reached 83 points with 
2 games left. [Match 35 - 80], [M36-83 ]. 

"""

"""
https://realpython.com/linear-regression-in-python/ I used this to learn how I can apply
Linear regression in Python using the sklearn library
"""