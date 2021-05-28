# -*- coding: utf-8 -*-
"""
Created on Sun May 16 19:42:35 2021

@author: Akshay Prakash
"""

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

#This line makes us show the chart in notebook 
table = pd.read_csv(r'C:\Users\Akshay Prakash\Downloads\1617table.csv')
table.head()
#.bar() argument plots our data {2 arguments_ x and height}
plt.bar(x=np.arange(1,21), height = table['Pts'])
#lets add title 
plt.title("Premier league 16/17")

plt.xticks(np.arange(1,21), table['team'], rotation = 90)
#Give the x and y axes a title 
plt.xlabel("Team")
plt.ylabel("Points")
#Given names Team and Points using xlabel and ylabel 
#Named all units on the x axis as names using plt.ticks(2 arguments - position, label values and rotation)
plt.show()
#Colors
teamColours = ['#034694','#001C58','#5CBFEB','#D00027',
              '#EF0107','#DA020E','#274488','#ED1A3B',
               '#000000','#091453','#60223B','#0053A0',
               '#E03A3E','#1B458F','#000000','#53162f',
               '#FBEE23','#EF6610','#C92520','#BA1F1A']
plt.bar(x=np.arange(1,21), height = table['Pts'], color = teamColours)
plt.xticks(np.arange(1,21), table['team'], rotation = 90)
plt.title("Premier league 16/17")
plt.xlabel("TEAMS")
plt.ylabel("Points")


