import csv
import pandas as pd
import re


movie= pd.read_csv('Data/movies_awards.csv',encoding ='latin1')

awards=pd.DataFrame(columns=["Awards","Awards_Won","Awards_Nominated","Prime_Awards_Nominated","Oscar_Awards_Nominated","Golden_Globe_Awards_Nominated","BAFTA_Awards_Nominated","Prime_Awards_won","Oscar_Awards_won","Golden_Globe_Awards_won","BAFTA_Awards_won"])
awards['Awards'] = movie['Awards'].dropna()
# awards.set_index('Awards',inplace=True)

# Getting digits from the awards column

awards['Awards_Won'] = movie['Awards'].apply(lambda x: (re.findall(r"(\d+) win", str(x))))
awards['Awards_Nominated'] = movie['Awards'].apply(lambda x: (re.findall(r"(\d+) nomination", str(x))))
awards['Prime_Awards_Nominated'] = movie['Awards'].apply(lambda x: (re.findall(r"Nominated for (\d+) Primetime Emmy", str(x))))
awards['Prime_Awards_won'] = movie['Awards'].apply(lambda x: (re.findall(r"Won (\d+) Primetime Emmy", str(x))))
awards['Oscar_Awards_Nominated'] = movie['Awards'].apply(lambda x: (re.findall(r"Nominated for (\d+) Oscar", str(x))))
awards['Oscar_Awards_won'] = movie['Awards'].apply(lambda x: (re.findall(r"Won (\d+) Oscar", str(x))))
awards['Golden_Globe_Awards_Nominated'] = movie['Awards'].apply(lambda x: (re.findall(r"Nominated for (\d+) Golden Globe", str(x))))
awards['Golden_Globe_Awards_won'] = movie['Awards'].apply(lambda x: (re.findall(r"Won (\d+) Golden Globe", str(x))))
awards['BAFTA_Awards_Nominated'] = movie['Awards'].apply(lambda x: (re.findall(r"Nominated for (\d+) BAFTA", str(x))))
awards['BAFTA_Awards_won'] = movie['Awards'].apply(lambda x: (re.findall(r"Won for (\d+) BAFTA", str(x))))

# Removing all the list and fill empty list with zero
# First column is awards name so skip first column and converting all to int
firstline = True
for a in awards.columns:
    if firstline:
        firstline = False
        continue
    awards[a] = (awards[a].apply(lambda x: 0 if len(x) == 0 else "".join(x))).astype(int)

# awards['Awards_Won']=awards['Awards_Won'].apply(lambda x :0 if len(x)==0 else"".join(x))
# awards['Awards_Nominated']=awards['Awards_Nominated'].apply(lambda x :0 if len(x)==0 else"".join(x))
# awards['Prime_Awards_Nominated']=awards['Prime_Awards_Nominated'].apply(lambda x :0 if len(x)==0 else"".join(x))
# awards['Prime_Awards_won']=awards['Prime_Awards_won'].apply(lambda x :0 if len(x)==0 else"".join(x))
# awards['Oscar_Awards_Nominated']=awards['Oscar_Awards_Nominated'].apply(lambda x :0 if len(x)==0 else"".join(x))
# awards['Oscar_Awards_won']=awards['Oscar_Awards_won'].apply(lambda x :0 if len(x)==0 else"".join(x))
# awards['Golden_Globe_Awards_Nominated']=awards['Golden_Globe_Awards_Nominated'].apply(lambda x :0 if len(x)==0 else"".join(x))
# awards['Golden_Globe_Awards_won']=awards['Golden_Globe_Awards_won'].apply(lambda x :0 if len(x)==0 else"".join(x))
# awards['BAFTA_Awards_Nominated']=awards['BAFTA_Awards_Nominated'].apply(lambda x :0 if len(x)==0 else"".join(x))
# awards['BAFTA_Awards_won']=awards['BAFTA_Awards_won'].apply(lambda x :0 if len(x)==0 else"".join(x))

# Summation of all the won and Nomination
awards['Awards_Won'] = awards['Awards_Won'] + awards['Prime_Awards_won'] + awards['Oscar_Awards_won'] + awards['Golden_Globe_Awards_won'] + awards['BAFTA_Awards_won']
awards['Awards_Nominated'] = awards['Awards_Nominated'] + awards['Prime_Awards_Nominated'] + awards['Oscar_Awards_Nominated'] + awards['Golden_Globe_Awards_Nominated'] + awards['BAFTA_Awards_Nominated']
awards.reset_index('Awards',inplace=True,drop=True)

awards.to_csv('CSV/Q4_P1.csv')
print(awards)