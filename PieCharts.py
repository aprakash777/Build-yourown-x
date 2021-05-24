# -*- coding: utf-8 -*-
"""
Created on Tue May 18 11:43:30 2021

@author: Akshay Prakash
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
leagueWins = {'Team':['Manchester United','Blackburn Rovers','Arsenal',
                     'Chelsea','Manchester City','Leicester City'],
             'Titles':[13,1,3,4,2,1]}
df = pd.DataFrame(leagueWins, columns =['Team', 'Titles'])
print(df)
#plt.pie()
#plt.pie(df['Titles'])
#plt.tight_layout()
#Create a list of the colours used for the teams, in order.
teamColours=['#f40206','#0560b5','#ce0000','#1125ff','#28cdff','#091ebc']
plt.pie(df['Titles'], labels = df['Team'], colors = teamColours, startangle=90)
plt.title("Premier league Titles")
plt.tight_layout()
