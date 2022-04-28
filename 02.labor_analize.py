#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 20:58:59 2022

@author: sedrakbarseghyan
"""

import pandas as pd
import matplotlib.pyplot as plt

#  Reading a csv file, which will be Panda's DataFrame object.

laborforce=pd.read_csv("cleaned_labor.csv", index_col="Occupation")

#  Sorting the Dataframe based on the number of jobs to be created in 2030 so 
#  that we can find the largest increasing and declining occupations in the 
#  future steps.

laborforce=laborforce.sort_values(by=["Emp_Change"])

total=laborforce["Emp_2020"].sum()
print(total)
total1=laborforce["Emp_2030"].sum()
print(total1)


#  Spliting the dataframe into three dataframes based on the absolute numbers: 
#  1) dataframe with the data where the number of jobs for specific occupations 
#  will remain the same in 2030
#  2) dataframe with the data where the number of jobs for specific occupations
#  will increase in 2030 
#  3) dataframe with the date where the number of jobs for specific occupations 
#  will decrease in 2030

no_change=laborforce.query("Emp_Change == 0")
increase=laborforce.query("Emp_Change >0")
decrease=laborforce.query("Emp_Change < 0")
print("Total number of occupations with no change in job quantity:",no_change["Emp_Change"].count())
print("Total number of occupations with job increase:",increase["Emp_Change"].count())
print("Total number of occupations with job decrease:",decrease["Emp_Change"].count())

#  Spliting the dataframe in the same way, like in the previous step, but in
#  this case using the percentages instead of absolute number of jobs created 
#  in the future.

no_change_p=laborforce.query("Emp_Change_P == 0")
increase_p=laborforce.query("Emp_Change_P >0")
decrease_p=laborforce.query("Emp_Change_P < 0")
print("Total number of occupations with no change in job quantity:",no_change_p["Emp_Change_P"].count())
print("Total number of occupations with job increase:",increase_p["Emp_Change_P"].count())
print("Total number of occupations with job decrease:",decrease_p["Emp_Change_P"].count())

#  Calculating the total number of job increase, decrease and net surplus in 
#  2030.

tot_incr=round(increase["Emp_Change"].sum()*1000)
tot_decr=round(decrease["Emp_Change"].sum()*1000)
overall=tot_incr+tot_decr
print("Total number of job increase in 2030:",f"{tot_incr:,}")
print("Total number of job decrease in 2030:",f"{tot_decr:,}")
print("Total difference:",f"{overall:,}")

#  Calculating the percentage change of job increase in 2030 in relation to
#  job quantity in 2020.

change=100*overall/(laborforce["Emp_2020"].sum()*1000)
print("Percentage change increase of future jobs:",round(change,2))

#  Creating 5 Series which represent 1) occupations whose job quantity will
#  not change in 2030, 2) ten occupations which will have the largest 
#  increase in job quantity in 2030 in absolute number, 3) ten occupations 
#  which will have largest decline in job quantity in 2030 in absolute numbers,
#  4) ten occupations which which will have the largest increase in job 
#  quantity as a percentage share, 5) ten occupations which which will have 
#  the largest decline in job quantity as a percentage share.

same=no_change["Emp_Change"]

top_occupations=increase["Emp_Change"].sort_values().nlargest(n=10)
bottom_occupations=decrease["Emp_Change"].sort_values().nsmallest(n=10)

top_occupations_p=increase_p["Emp_Change_P"].sort_values().nlargest(n=10)
bottom_occupations_p=decrease_p["Emp_Change_P"].sort_values().nsmallest(n=10)

#  Printing the occupations whose employment remains the same to familiarize
#  with that list.

print(same)

#  Creating 4 figures which represent the top ten largest growing occupations 
#  by absolute numbers and percentage shares, and the top ten largest 
#  declining occupations by absolute numbers and percentage shares.

fig1,ax1=plt.subplots(dpi=300)
top_occupations.plot.barh(ax=ax1, y="Occupation", x="Emp_Change")
fig1.suptitle("Ten Largest Job Creating Occupations, Thousands")
ax1.set_xlabel("")
ax1.set_ylabel("")
ax1.annotate(round(top_occupations[9]),(400,8.8),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(top_occupations[8]),(400,7.7),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(top_occupations[7]),(400,6.7),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(top_occupations[6]),(460,5.8),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(top_occupations[5]),(500,4.8),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(top_occupations[4]),(570,3.8),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(top_occupations[3]),(600,2.8),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(top_occupations[2]),(700,1.8),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(top_occupations[1]),(800,0.8),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(top_occupations[0]),(800,-0.2),textcoords="offset points",xytext=(0,0),ha="center",color="white")
fig1.tight_layout()
fig1.savefig("fig1_largest_increase.png")

fig1,ax1=plt.subplots(dpi=300)
bottom_occupations.plot.barh(ax=ax1)
fig1.suptitle("Ten Largest Job Cutting Occupations, Thousands")
ax1.set_xlabel("")
ax1.set_ylabel("")
ax1.annotate(round(bottom_occupations[9]),(-80,8.85),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(bottom_occupations[8]),(-90,7.8),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(bottom_occupations[7]),(-100,6.8),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(bottom_occupations[6]),(-115,5.8),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(bottom_occupations[5]),(-125,4.8),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(bottom_occupations[4]),(-135,3.8),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(bottom_occupations[3]),(-140,2.8),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(bottom_occupations[2]),(-155,1.8),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(bottom_occupations[1]),(-215,0.8),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(bottom_occupations[0]),(-290,-0.2),textcoords="offset points",xytext=(0,0),ha="center",color="white")
fig1.tight_layout()
fig1.savefig("fig2_largest_decline.png")

fig1,ax1=plt.subplots(dpi=300)
top_occupations_p.plot.barh(ax=ax1, y="Occupation", x="Emp_Change")
fig1.suptitle("Ten Fastest Growing Occupations by Percentage Change")
ax1.set_xlabel("")
ax1.set_ylabel("")
ax1.annotate(round(top_occupations_p[9]),(47,8.8),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(top_occupations_p[8]),(47,7.8),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(top_occupations_p[7]),(53,6.8),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(top_occupations_p[6]),(56,5.8),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(top_occupations_p[5]),(58,4.8),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(top_occupations_p[4]),(61,3.8),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(top_occupations_p[3]),(61,2.8),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(top_occupations_p[2]),(66.7,1.8),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(top_occupations_p[1]),(63,0.8),textcoords="offset points",xytext=(0,0),ha="center",color="white")
ax1.annotate(round(top_occupations_p[0]),(63,-0.2),textcoords="offset points",xytext=(0,0),ha="center",color="white")
fig1.tight_layout()
fig1.savefig("fig3_largest_increase_p.png")

fig1,ax1=plt.subplots(dpi=300)
bottom_occupations_p.plot.barh(ax=ax1)
fig1.suptitle("Ten Fastest Declining Occupations by Percentage Change")
ax1.set_xlabel("")
ax1.set_ylabel("")
ax1.annotate(round(bottom_occupations_p[9]),(-26,8.85),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(bottom_occupations_p[8]),(-26.5,7.8),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(bottom_occupations_p[7]),(-27.5,6.8),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(bottom_occupations_p[6]),(-28.5,5.8),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(bottom_occupations_p[5]),(-29,4.8),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(bottom_occupations_p[4]),(-29.5,3.8),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(bottom_occupations_p[3]),(-33,2.8),textcoords="offset points",xytext=(0,0),ha="center")
ax1.annotate(round(bottom_occupations_p[2]),(-30,1.8),textcoords="offset points",xytext=(0,0),ha="center",color="white")
ax1.annotate(round(bottom_occupations_p[1]),(-30,0.8),textcoords="offset points",xytext=(0,0),ha="center",color="white")
ax1.annotate(round(bottom_occupations_p[0]),(-30,-0.2),textcoords="offset points",xytext=(0,0),ha="center",color="white")
fig1.tight_layout()
fig1.savefig("fig4_largest_decline_p.png")