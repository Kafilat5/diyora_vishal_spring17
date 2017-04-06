import pandas as pd
import numpy as np

#Loading CSV
employee=pd.read_csv('Data/employee_compensation.csv')
#Group by Organization and Department
employee_group=employee.groupby(['Organization Group','Department']).agg({'Total Compensation': np.average})

#sort by the total Compensation
employee_sort= employee_group['Total Compensation'].groupby(level=0, group_keys=False)
res = employee_sort.apply(lambda x: x.sort_values(ascending=False))

compensation=res.to_frame()
compensation.to_csv('CSV/Q2_P1.csv')
print(compensation.head())
