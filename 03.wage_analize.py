#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 17:19:28 2022

@author: sedrakbarseghyan
"""


import pandas as pd
import matplotlib.pyplot as plt

#  Reading a csv file, which will be Panda's DataFrame object.

labor=pd.read_csv("cleaned_labor.csv", index_col="Occupation", thousands=",")

#  Creating 5 quintile groups based on the "Wage" column, grouping 
#  "Emp_Change" column based on those quintiles, and then summing up the
#  results. The purpose is to calculate the number of jobs created in the 
#  future according to 5 wage groups(quintiles): 1 is the lowest and 5 is the 
#  highest quintile. The printing the threshold wage levels of those quintiles
#  to understand the wage range for these quintiles.

labor["quint"]=pd.qcut(labor["Wage"],5,labels=[1,2,3,4,5])
quintiles=labor["Emp_Change"].groupby(labor["quint"]).sum()
quint_threshold=labor["Wage"].groupby(labor["quint"]).max()
print(quint_threshold)
#  Now transforming the results of the previos step into percentages.

total=labor["Emp_Change"].sum()
quint_percent=100*quintiles/total

#  Creating a two-panel figure to show the number and percentage of future job 
#  growth based on the five wage quintiles, which reveals that the lowest 
#  quintile has the largest number of future jobs.

fig,(ax1,ax2)=plt.subplots(1,2,dpi=300)
fig.suptitle("Distribution of New Created Jobs by Wage Quintiles")
quint_percent.plot.bar(ax=ax1, fontsize=7)
ax1.set_ylabel("Percentage")
ax1.annotate(round(quint_percent[1]),(0.2,45),textcoords="offset points",xytext=(0,0),ha="right")
ax1.annotate(round(quint_percent[2]),(1.1,9),textcoords="offset points",xytext=(0,0),ha="right")
ax1.annotate(round(quint_percent[3]),(2.2,12),textcoords="offset points",xytext=(0,0),ha="right")
ax1.annotate(round(quint_percent[4]),(3.2,16),textcoords="offset points",xytext=(0,0),ha="right")
ax1.annotate(round(quint_percent[5]),(4.2,22),textcoords="offset points",xytext=(0,0),ha="right")
quintiles.plot.barh(ax=ax2, fontsize=7)
ax2.set_xlabel("Thousands")
ax2.annotate(round(quintiles[1]),(4000,-0.1),textcoords="offset points",xytext=(0,0),ha="left", color="white")
ax2.annotate(round(quintiles[2]),(1100,0.9),textcoords="offset points",xytext=(0,0),ha="left")
ax2.annotate(round(quintiles[3]),(1500,1.9),textcoords="offset points",xytext=(0,0),ha="left")
ax2.annotate(round(quintiles[4]),(1900,2.9),textcoords="offset points",xytext=(0,0),ha="left")
ax2.annotate(round(quintiles[5]),(2700,4),textcoords="offset points",xytext=(0,0),ha="left")
fig.tight_layout()
fig.savefig('fig5_quintiles.png')
        
        
        