#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 14:07:18 2022

@author: sedrakbarseghyan
"""

import pandas as pd

#  Reading a csv file, which will be Panda's DataFrame object.

education=pd.read_csv("TrendGenerator-Table-All-Years.csv", header=2, index_col=0)

#  Printing the row names of the Dataframe so that we can drop unnecessary
#  rows in the next step.

print("Row names of DataFrame:",list(education.index))

#  Dropping the rows which will not be used for this analysis, i.e. dropping
#  all data for the years 2009 and 2010, so that our data can include the 
#  decade (10-year-period) from 2011 to 2020 including.This data will be used
#  as a projected number of degrees for 2021-2030. 

education=education.drop([2010,2009])

#  Printing the column names of a Dataframe to drop unnecessary columns in the
#  next step.

print("Column names of DataFrame:",list(education.columns))

#  Dropping all unnecessary columns of the Dataframe which will not be used
#  for this analysis, as a result keeping only the "Award level" and "Total"
#  columns.

education=education[["Award level","Total"]]

#  Now converting the "Total" column of dataframe to integers so that we can
#  make necessary calculations.

education["Total"]=education["Total"].str.replace(",","").astype(int)

#  The data has three different rows for doctoral and professional degrees
#  with the following steps we are combining those three rows in one row
#  with the name "Doctoral or professional degree", at the same summing
#  their values for "Total" column, so that we will have combined number of
#  doctoral or professional degrees for each year.

education["Award level"]=education["Award level"].replace({"Doctor's degree - research/scholarship (new degree classification)":"Doctoral or professional degree","Doctor's degree - professional practice (new degree classification)":"Doctoral or professional degree","Doctor's degree - other (new degree classification)":"Doctoral or professional degree"})
education=education.groupby(["Year","Award level"]).sum()

#  Reseting index column of the dataframe to recover Year and Award level
#  columns.

education=education.reset_index()
                                 
#  Keeping in a dataframe only the data related to the degrees (associate, 
#  bachelor, master and PhD/professional degrees), because in the 
#  future analysis we should compare those numbers with the employment data 
#  numbers where only those mentioned educational attainment levels are 
#  available. 

education=education.loc[education["Award level"].str.endswith("degree")].groupby("Award level").sum()

#  The "Total" column is devided by 1000, because in the future analysis 
#  it will be more convenient and harmonised with the employment database 
#  which is also in thousands.

education["Total"]=round(education["Total"]/1000)

#  Dropping the "Year" column which is not necessary, renaming the Total column
#  to Degrees and writing the result in a csv file. 

education=education.drop(columns="Year").rename(columns={"Total":"Degrees"})
education.to_csv("cleaned_education.csv")




