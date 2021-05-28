# -*- coding: utf-8 -*-
"""
Created on Sun May 23 06:51:25 2021
@author: Akshay Prakash
"""
#This program basically consists of concantenations of DataFrames
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 

df1 = pd.read_csv(r'\F9596PL.csv')
df2 = pd.read_csv(r'\F9697PL.csv')
df3= pd.read_csv(r'\F9798PL.csv')
df4 = pd.read_csv(r'\F9899PL.csv')
df5= pd.read_csv(r'\F9900PL.csv')
df6 = pd.read_csv(r'\F0001PL.csv')
df7 = pd.read_csv(r'\F0102PL.csv')
df8 = pd.read_csv(r'\F0203PL.csv')
frame = [df1,df2,df3,df4,df5,df6,df7,df8]
result = pd.concat(frame)


df9 = pd.read_csv(r'\F0304PL.csv')
df10 = pd.read_csv(r'\F0405PL.csv')
df11 = pd.read_csv(r'\F0506PL.csv')
df12 = pd.read_csv(r'\F0607PL.csv')
df13 = pd.read_csv(r'\F0708PL.csv')
df14 = pd.read_csv(r'\F0809PL.csv')
df15 = pd.read_csv(r'\F0910PL.csv')

frame1 = [df9, df10,df11,df12,df13,df14, df15]
result1 = pd.concat(frame1)

df16 = pd.read_csv(r'\F1011PL.csv')
df17 = pd.read_csv(r'\F1112PL.csv')
df18 = pd.read_csv(r'\F1213PL.csv')
df19 = pd.read_csv(r'\F1314PL.csv')
df20 = pd.read_csv(r'\F1415PL.csv')
df21 = pd.read_csv(r'\F1516PL.csv')
df22 = pd.read_csv(r'\F1617PL.csv')
df23 = pd.read_csv(r'\F1718PL.csv')
df24 = pd.read_csv(r'\F1819PL.csv')
df25 = pd.read_csv(r'\F1920PL.csv')
frame2 = [df16, df17,df18,df19,df20,df21,df22,df23,df24,df25]
result2 = pd.concat(frame2)

Result = [df1,df2,df3,df4,df5,df6,df7,df8,df9,df10, df11, df12, df13, df14, df16, df17, df18, df19,
          df20,df21,df22,df23,df24,df25]

df = pd.concat(Result)


"""
Here, I have used concantenation to Join all DataFrames. Make sure to open this while executing your Project as you'll need to import the file 
or even use the varibles. For example, you might want to use "result2" for plotting F1011Pl to F1920PL
"""

