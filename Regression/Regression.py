# -*- coding: utf-8 -*-
"""
Created on Sun May 23 06:51:25 2021

@author: Akshay Prakash
"""

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 

df1 = pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\F9596PL.csv')
df2 = pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\F9697PL.csv')
df3= pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\F9798PL.csv')
df4 = pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\F9899PL.csv')
df5= pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\F9900PL.csv')
df6 = pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\F0001PL.csv')
df7 = pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\F0102PL.csv')
df8 = pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\F0203PL.csv')
frame = [df1,df2,df3,df4,df5,df6,df7,df8]
result = pd.concat(frame)


df9 = pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\F0304PL.csv')
df10 = pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\F0405PL.csv')
df11 = pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\F0506PL.csv')
df12 = pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\F0607PL.csv')
df13 = pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\F0708PL.csv')
df14 = pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\F0809PL.csv')
#df15 = pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\F0910PL.csv')

frame1 = [df9, df10,df11,df12,df13,df14] #df15]
result1 = pd.concat(frame1)

df16 = pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\F1011PL.csv')
df17 = pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\F1112PL.csv')
df18 = pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\F1213PL.csv')
df19 = pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\F1314PL.csv')
df20 = pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\F1415PL.csv')
df21 = pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\F1516PL.csv')
df22 = pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\F1617PL.csv')
df23 = pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\F1718PL.csv')
df24 = pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\F1819PL.csv')
df25 = pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\F1920PL.csv')
frame2 = [df16, df17,df18,df19,df20,df21,df22,df23,df24,df25]
result2 = pd.concat(frame2)

Result = [df1,df2,df3,df4,df5,df6,df7,df8,df9,df10, df11, df12, df13, df14, df16, df17, df18, df19,
          df20,df21,df22,df23,df24,df25]

df = pd.concat(Result)

# print(df['Pts'])
# y = df.Rk
# x = df.Pts.values.reshape(-1,1) #.values with reshape because its DF 
# print(x.shape, y.shape) #(rows,colums)
# model = LinearRegression().fit(x, y)
# r_sqrt = model.score(x,y)
# print('r_sqrt: ', r_sqrt)
# intercept = model.intercept_
# slope = model.coef_
# print('intercept: ', intercept)
# print('slope: ', slope)
# y_predicted = intercept + slope* x #Linear Regression eqn
# fig, ax = plt.subplots(figsize = (10,10))
# plt.scatter(x,y, color = 'blue', label = 'Points')
# plt.plot(x,y_predicted, color = 'red', label = 'Linear Regression')
# plt.legend()
# plt.ylim(0.5, 20.5) #dont do 0 because there's no 0 position
# plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]) 
# plt.gca().invert_yaxis()#rewrite because it should be from low to high
# plt.xlabel('Points')
# plt.ylabel('League Position')
# plt.title('Evaluating relationship between Points and league position')
# plt.text(10, 3, "Slope: -0.332 ", color = 'red', size= '15')
# plt.text(10, 3.7, f'Intercept: {intercept}', color = 'red', size= '15')
# plt.text(10, 4.4, f'r_sqrt: {r_sqrt}', color = 'red', size= '15')
# plt.text(92, 1.4, "Man City 18/19 (98)", color ='red', size = '7')
# plt.text(92, 2.4, "Liverpool 18/19 (97)", color ='red', size = '7')
# plt.text(7, 19.6, "Derby County 2008/09 ", color = 'red', size= '7')

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


