# Employment Projections in the USA for 2030
 
@author: sedrakbarseghyan
"""

# Final Project: Analyzing the Employment Projections in the USA for 2020-2030

## Summary

This project examines the employment projections (growth) in the USA for 2020-2030 analyzing the fastest growing and largest declining occupation trends, job growth based on quintiles, as well as analyzing the degree supply and demand to fill in the growing number of jobs for that decade. 

## Input Data

There are two input data for this project. Both are CSV files. The first file, called **Employment-Projections.csv**, is available in the US Bureau of Labor Statistics website (**https://data.bls.gov/projections/occupationProj)** . This data represents the employment statistics in 2020 and the projection for the next 10 years (until 2030) based on 790 occupations. The data includes number of jobs in 2020, the median annual wage, projected number of job change in 2030, typical entry level education and some other data which will not be used for this analysis.

The second CSV file called **TrendGenerator-Table-All-Years.csv** is available in the National Center for Education Statistics website (https://nces.ed.gov/ipeds/TrendGenerator/app/answer/4/24). This data represents the number of degrees/certificates awarded at postsecondary institutions in the United States from 2009 to 2020. This data will be used to calculate the quantity of degrees awarded from 2011 to 2020 which will be used to project the number of degrees awarded for the 10-year period from 2021-2030 (for this project we will assume that the number of degress for 2021-2030 will be the same as for 2011-2020).

## Outputs 

The project has the following outputs:

1) five scripts, which should be run in the following order:

    1. The first script, called **01.labor-clean.py**, reads the first input data (Employment-Projections.csv), builds a Pandas dataframe, eliminates unnecessary columns, renames some columns, corrects some mistakes, in other words, cleans the data and writes the dataframe out in a csv form.
    
    2. The second script, called **02.labor_analyze.py**, reads in the csv file created by the previous script, calculates total employment, the difference in employment between 2020 and 2030, finds out the total number of occupations (both in absolute and percentage values) which will have job increase, decrease or same number of jobs within the period of 10 years, reveals the occupations which will not change the job quantity, top ten fastest growing and top ten fastest declining occupations based on percentage change, ten largest job creating occupations and ten largest job reducing occupations, and produces 4 appropriate figures.
    
    3. The third script, called **03.wage_analyze.py**, creates five quintile groups based on the median wages presented in the database, groups the occupations and calculates the number of jobs created from 2020-2030 based on that five quintiles, and writes out the results in a figure.
    
    4. The forth script, called **04.education-clean.py**, reads the second input data (TrendGenerator-Table-All-Years.csv), builds a Pandas dataframe, eliminates unnecessary columns and rows, combines 3 types of doctoral and professional degrees, in other words, cleans the data, aggregates the total number of degrees awarded by 4 types of educational attainment: associate, bachelor, master and PhD/professional degrees, and writes the dataframe out in a csv form.
    
    5. The fifth script, called **05.education_analyze.py**, reads in the csv file created by the previous script, creats a figure to show the result of job change in the future based on the level of education, groups the data and calculates the average, median, maximum and minimum percentage change for each educational level, creates a heatmap figure to show the result of this calculations, merges both datadrames to calculate the difference between the number of projected degrees awarded 2021-2030 and the number of degress required to fill the growing number of jobs from 2020 to 2030, and creating a figures to show that contrast. 

2) two csv files `"cleaned_labor.csv"` and `"cleaned_education.csv"` which are cleaned files produced by the **01.labor-clean.py** and **04.education-clean.py** scripts

3) 9 figures:
    01 bar graph for the ten largest job creating occupations in absolute numbers (`"fig1_largest_increase.png"`);
    02 bar graph for the ten largest job cutting occupations in absolute numbers (`"fig2_largest_decline.png"`);
    03 bar graph for the ten fastest growing occupations based on percentages (`"fig3_largest_increase_p.png"`);
    04 bar graph for the ten fastest declining  occupations based on percentages (`"fig4_largest_decline_p.png"`);
    05 two-panel bar graph for the future job increase by wage quintiles (`"fig5_quintiles.png"`);
    06 bar graph for the quantity of new jobs according to the level of education (`"fig6_education_numbers.png"`);
    07 heatmap graph for the employment change statistics based on grouped educational attainments (`"fig7_education_percentages.png"`);
    08 two-panel bar graph for the available and required number of gegrees to fill new jobs for 2020-2030 (`"fig8_degree_supply_demand.png"`);
    09 two-panel bar graph for the degree surplus for 2020-2030 (`"fig9_degree_surplus.png"`);

## Results

The project has the following results
