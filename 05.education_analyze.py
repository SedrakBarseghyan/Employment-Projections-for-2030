#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 20:47:41 2022

@author: sedrakbarseghyan
"""


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#  Reading a csv file, which will be Panda's DataFrame object.

labor=pd.read_csv("cleaned_labor.csv", index_col="Occupation", thousands=",")

#  Creating a dataframe from the csv file, which composed of two columns: 
#  "Employment Change" and "Education level". These are the only columns
#  which will be needed for this analysis. Then grouping this dataframe by 
#  educational level and calculating how many jobs will be created in 2030
#  for each educational level.

group_educ_change=labor[["Emp_Change",'Educ_Level']].assign().groupby(['Educ_Level'])
grouped_educ_change=round(group_educ_change.sum()).sort_values(by="Emp_Change")

#  Creating a single-panel figure to show the result of job change in the 
#  future based on the level of education.


fig1,ax1=plt.subplots(dpi=300)
grouped_educ_change.plot.barh(ax=ax1)
fig1.suptitle("The Quantity of New Jobs according to the Level of Education, Thousands")
ax1.annotate(round(grouped_educ_change["Emp_Change"][7]),(3400,6.9),textcoords="offset points",xytext=(0,0),ha="center", color="white")
ax1.annotate(round(grouped_educ_change["Emp_Change"][6]),(3400,5.9),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(grouped_educ_change["Emp_Change"][5]),(3400,4.9),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(grouped_educ_change["Emp_Change"][4]),(1300,3.9),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(grouped_educ_change["Emp_Change"][3]),(800,2.9),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(grouped_educ_change["Emp_Change"][2]),(760,1.8),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(grouped_educ_change["Emp_Change"][1]),(700,0.8),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(grouped_educ_change["Emp_Change"][0]),(500,-0.1),textcoords="offset points",xytext=(0,0),ha="center")
ax1.set_xlabel("")
ax1.set_ylabel("")
fig1.tight_layout()
fig1.savefig("fig6_education_numbers.png")


#  Creating and grouping the dataframe, like in the previous step, but this 
#  time using percentage change of jobs instead of absolute numbers. Based on
#  that dataframe calculating the average, median, maximum and minimum 
#  percentage change for each educational level. Then dropping the 
#  "Emp_Change_P" column to have clear results, which will be used to create
#  a figure in the next step.

group_educ_change_p=labor[["Emp_Change_P",'Educ_Level']].assign().groupby(['Educ_Level'])
grouped_educ_change_p=group_educ_change_p.mean().sort_values(by="Emp_Change_P")
grouped_educ_change_p["Mean"]=round(group_educ_change_p.mean(),1)
grouped_educ_change_p["Median"]=group_educ_change_p.median()
grouped_educ_change_p["Min"]=group_educ_change_p.min()
grouped_educ_change_p["Max"]=group_educ_change_p.max()
grouped_educ_change_p=grouped_educ_change_p.drop(columns="Emp_Change_P")

#  Creating a single-panel heatmap figure to show the percentage change of
#  future jobs based on the educational level.

fig,ax1=plt.subplots(dpi=300)
fig.suptitle("Employment Change Statistics Based on Grouped Educational Attainments, Percentages")
sns.heatmap(grouped_educ_change_p, annot=True, fmt=".1f", ax=ax1)
ax1.set_xlabel("")
ax1.set_ylabel("")
fig.tight_layout()
fig.savefig("fig7_education_percentages.png")

#  Reading a csv file for education, which will be Panda's DataFrame object, 
#  and then merging that data with the grouped dataframe created above to make
#  comparison. Then dropping the merged column, which is not useful here.

education=pd.read_csv("cleaned_education.csv")
educ=grouped_educ_change.merge(education,
                     left_on="Educ_Level", 
                     right_on="Award level",
                     how="inner",
                     validate="1:1",
                     indicator=True)
educ=educ.set_index("Award level").drop(columns="_merge")

#  Now calculating the difference between the number of projected degrees 
#  awarded 2021-2030 and the number of degress required to fill the growing 
#  number of jobs from 2020  to 2030. The calculation is done both for absolute 
#  and percentage values.

educ["Degree_Diff"]=educ["Degrees"]-educ["Emp_Change"]
educ["Degree_Diff_P"]=round(educ["Degree_Diff"]*100/educ["Degrees"])
educ=educ.sort_values(by=["Degree_Diff_P"])

#  Finally creating a two two-panel figures to show the contrast of the 
#  projected number of future degrees and the total number of degrees needed
#  to fill the jobs in the future. And the second figure shows the demand for 
#  additional degrees in 2030 in absolute numbers and percentages.

fig,(ax1,ax2)=plt.subplots(1,2,dpi=300)
fig.suptitle("Available and Required Number of Degrees to fill new jobs for 2020-2030, Thousands")
educ["Degrees"].plot.bar(ax=ax1, fontsize=7, color=["lightcyan","paleturquoise","lightseagreen","darkcyan"])
ax1.set_xlabel("AVAILABLE")
ax1.annotate(round(educ["Degrees"][0]),(0.3,2600),textcoords="offset points",xytext=(0,0),ha="right")
ax1.annotate(round(educ["Degrees"][1]),(1.4,12000),textcoords="offset points",xytext=(0,0),ha="right")
ax1.annotate(round(educ["Degrees"][2]),(2.3,8800),textcoords="offset points",xytext=(0,0),ha="right")
ax1.annotate(round(educ["Degrees"][3]),(3.35,11000),textcoords="offset points",xytext=(0,0),ha="right")
educ["Emp_Change"].plot.bar(ax=ax2, fontsize=7, color=["lightcyan","paleturquoise","lightseagreen","darkcyan"])
ax2.set_xlabel("REQUIRED")
ax2.annotate(round(educ["Emp_Change"][0]),(0,500),textcoords="offset points",xytext=(0,0),ha="center")
ax2.annotate(round(educ["Emp_Change"][1]),(1,700),textcoords="offset points",xytext=(0,0),ha="center")
ax2.annotate(round(educ["Emp_Change"][2]),(2,550),textcoords="offset points",xytext=(0,0),ha="center")
ax2.annotate(round(educ["Emp_Change"][3]),(3,430),textcoords="offset points",xytext=(0,0),ha="center")
fig.tight_layout()
fig.savefig("fig8_degree_supply_demand.png")


fig,(ax1,ax2)=plt.subplots(1,2,dpi=300)
fig.suptitle("Degree Surplus for 2020-2030")
educ["Degree_Diff"].plot.bar(ax=ax1, fontsize=7, color=["lightsteelblue","cornflowerblue","royalblue","midnightblue"])
ax1.set_xlabel("THOUSANDS")
ax1.annotate(round(educ["Degree_Diff"][0]),(0.3,2000),textcoords="offset points",xytext=(0,0),ha="right")
ax1.annotate(round(educ["Degree_Diff"][1]),(1.35,11000),textcoords="offset points",xytext=(0,0),ha="right")
ax1.annotate(round(educ["Degree_Diff"][2]),(2.3,8200),textcoords="offset points",xytext=(0,0),ha="right")
ax1.annotate(round(educ["Degree_Diff"][3]),(3.3,10550),textcoords="offset points",xytext=(0,0),ha="right")
educ["Degree_Diff_P"].plot.bar(ax=ax2, fontsize=7, color=["lightsteelblue","cornflowerblue","royalblue","midnightblue"])
ax2.set_xlabel("PERCENTAGES")
ax2.annotate(round(educ["Degree_Diff_P"][0]),(0,80),textcoords="offset points",xytext=(0,0),ha="center")
ax2.annotate(round(educ["Degree_Diff_P"][1]),(1,82),textcoords="offset points",xytext=(0,0),ha="center")
ax2.annotate(round(educ["Degree_Diff_P"][2]),(2,83),textcoords="offset points",xytext=(0,0),ha="center", color="white")
ax2.annotate(round(educ["Degree_Diff_P"][3]),(3,84),textcoords="offset points",xytext=(0,0),ha="center",color="white")
fig.tight_layout()
fig.savefig("fig9_degree_surplus.png")
