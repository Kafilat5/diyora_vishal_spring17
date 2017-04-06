import pandas as pd
import numpy as np
import re


#Loading the file clean it by Year type
employee=pd.read_csv('Data/employee_compensation.csv')
employee_calendar=employee[employee['Year Type'] == 'Calendar']

#Make Employee Identifier sorted and making it as index So it is easy to compare with the other index
employee_sort=employee_calendar.sort_values(by='Employee Identifier')
employee_sort.set_index('Employee Identifier',inplace=True)

#sum of of Salaries and Overtime same employee identifier and removing the duplicate
employee_salary=employee_calendar.groupby(['Employee Identifier']).agg({'Salaries': np.sum,'Overtime': np.sum})

#People with more than 5% overtime of the salaries
employee_time=employee_salary[employee_salary['Overtime']/employee_salary['Salaries']>0.05]

#Comparing index with the index of the calendar year type and putting it in dataframe
employee_clean=employee_sort[employee_sort.index.isin(employee_time.index)]

#Groupby the Job Family name using the data frame got in above steps
employee_calendar1= employee_clean.groupby('Job Family').agg({'Total Benefits': np.average,'Total Compensation':np.average})

#Calculating percentage of total benefits to total compensation
employee_calendar1['Percentage']=(employee_calendar1['Total Benefits']/employee_calendar1['Total Compensation'])*100

employee_calendar1.to_csv('CSV/Q2_P2.csv')
print(employee_calendar1.head())