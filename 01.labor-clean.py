#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 09:23:53 2022

@author: sedrakbarseghyan
"""

import pandas as pd

#  Reading a csv file, which will be Panda's DataFrame object, which should 
#  be used for the analysis of this project.

projection=pd.read_csv("Employment-Projections.csv",thousands=",")

#  Printing the column names of the Dataframe so that we can drop unnecessary
#  columns in the next step.

print("Column names of DataFrame:",list(projection.columns))

#  Dropping unnecessary columns which will not be used for this analysis. 

projection=projection.drop(columns=["Occupation Code","Work Experience in a Related Occupation", 'Occupational Openings, 2020-2030 Annual Average', "Workex Code",'Education Code',"Typical on-the-job Training","trCode"])

#  Renaming some columns of the Dataframe to make them more convenient for 
#  our use.

projection=projection.rename(columns={"Occupation Title":"Occupation","Employment 2020":"Emp_2020", "Employment 2030":"Emp_2030", "Employment Change, 2020-2030":"Emp_Change", "Employment Percent Change, 2020-2030":"Emp_Change_P","Median Annual Wage 2020":"Wage","Typical Entry-Level Education":"Educ_Level"})

#  Shortening the names of occupations, more specifically in the "Occupation" 
#  column deleting all the strings which come after asterics and deleting
#  the unnecessary spaces resulted from that action. This step is needed to 
#  display the occupation names in user-friendly way, especially when 
#  displaying those occupations in figures.

projection["Occupation"]=projection["Occupation"].str.replace(r"\*.*","",regex=True)
projection["Occupation"]=projection["Occupation"].str.strip()

#  Checking for the duplicates of the names of occupations to be sure there
#  are no matches.

duplic=projection.duplicated(subset='Occupation', keep=False)
print('\nRecords with duplicate occupations:', projection[duplic].value_counts().sum())

#  Removing the non-digit characters from "Wage" column, more specifically
#  removing " >= " characters next to 208000 which will enable the future 
#  calculations based on theat column. With the same purpose filling in the 
#  missing values for "Wage" column, more specifically replacing 0 for all 
#  missing data i.

projection["Wage"]=projection["Wage"].str.replace(r'\D|\s','',regex=True)
projection["Wage"]=projection["Wage"].fillna(0)

#  Correcting some mistakes which have been revealed in a data. For the 
#  occupations which do not have any job growth or decline in 2030, the 
#  "Emp_Change_P" column mistakenly shows some percentage changes, which
#  actually have to be zero. So here we are replacing those wrong percentage 
#  values with zero.


projection.loc[projection["Occupation"]=="Fish and game wardens", 'Emp_Change_P'] = 0
projection.loc[projection["Occupation"]=="Geographers", 'Emp_Change_P'] = 0
projection.loc[projection["Occupation"]=="Embalmers", 'Emp_Change_P'] = 0
projection.loc[projection["Occupation"]=="Designers, all other", 'Emp_Change_P'] = 0
projection.loc[projection["Occupation"]=="Farm labor contractors", 'Emp_Change_P'] = 0
projection.loc[projection["Occupation"]=="Rail yard engineers, dinkey operators, and hostlers", 'Emp_Change_P'] = 0
projection.loc[projection["Occupation"]=="Rail transportation workers, all other", 'Emp_Change_P'] = 0

#  Writing the cleaned file to csv for future analysis

projection.to_csv("cleaned_labor.csv", index=False)




