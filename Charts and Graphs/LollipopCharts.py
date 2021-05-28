# -*- coding: utf-8 -*-
"""
Created on Mon May 17 21:24:53 2021

@author: Akshay Prakash
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

table = pd.read_csv(r'\1617table.csv')
table.head()
plt.hlines(y= np.arange(1, 21), xmin = 0, xmax = table['Pts'], color = 'skyblue')
plt.plot(table['Pts'], np.arange(1,21), "o")
plt.yticks(np.arange(1,21), table['team'])
plt.show()
teamColours = ['#034694','#001C58','#5CBFEB','#D00027',
              '#EF0107','#DA020E','#274488','#ED1A3B',
               '#000000','#091453','#60223B','#0053A0',
               '#E03A3E','#1B458F','#000000','#53162f',
               '#FBEE23','#EF6610','#C92520','#BA1F1A']
plt.hlines(y= np.arange(1, 21), xmin = 0, xmax = table['Pts'], color = teamColours)
plt.plot(table['Pts'], np.arange(1,21), "o")
plt.yticks(np.arange(1,21), table['team'])
plt.xlabel('Points')
plt.ylabel('Teams')
plt.title("Premier league 16/17")


