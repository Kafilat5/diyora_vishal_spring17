import pandas as pd
import csv
import calendar,os

try:
    os.mkdir('CSV')
except:
    pass
#Read file from csv
vehicle= pd.read_csv("Data/vehicle_collisions.csv")
with open('CSV/Q1_P1.csv','w') as csvfile:
    fieldnames = ['MONTH','MANHATTAN','NYC','PERCENTAGE']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for a in range(1,13):
        #Looping through each month
        year=vehicle[(vehicle['BOROUGH'] =="MANHATTAN") & (vehicle['DATE'].apply(lambda x:x.split("/")[2]) == "16") ]
        nyc=((vehicle['DATE'].apply(lambda x:x.split("/")[2]) == "16") & (vehicle['DATE'].apply(lambda x:x.split("/")[0]) == str(a))).sum()
        manhattan_acc=(year['DATE'].apply(lambda x:x.split("/")[0]) == str(a)).sum()
        percentage=manhattan_acc/nyc
#         print(percentage.round(8),nyc,manhattan_acc,calendar.month_name[int(a)][:3])
        writer.writerow({'MONTH':calendar.month_name[int(a)][:3],'MANHATTAN':manhattan_acc,'NYC':nyc,'PERCENTAGE':percentage.round(8)})
