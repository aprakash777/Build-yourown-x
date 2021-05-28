# -*- coding: utf-8 -*-
"""
Created on Tue May 18 10:44:34 2021

@author: Akshay Prakash
"""

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

table = pd.read_csv(r'\1617table.csv')
table.head()

#Creating chart with our own size
fig, ax = plt.subplots()
#Plot size
fig.set_size_inches(7,5)
#Add crosshairs
#Goals for on x axis, goals against on y axis, marked by "*"
plt.plot(table['gf'], table['ga'], "*")
#k means black - means draw line
plt.plot([table['gf'].mean(), table['gf'].mean()], [90,20], 'k-', linestyle = ':', lw=1)
#plt.plot([20,90], [table['ga'].mean(), table['ga'].mean()], 'k-', linestyle = ':', lw=1)
#add labels to chart area 
ax.set_title("Goals for & Goals against")
ax.set_xlabel("Goals for")
ax.set_ylabel("Goals against")
ax.text(18,90, "Poor attack Poor defense", color = 'red', size = '8')
ax.text(67,20, "Good attack Good defense", color = 'red', size = '8')
ax.text(20,20, "Poor attack Good defense", color = 'red', size = '8')
ax.text(67, 90, "Good attack Poor defense", color = 'red', size= '8')
plt.show()
