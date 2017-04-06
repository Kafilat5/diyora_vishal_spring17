import pandas as pd
import numpy as np
import ast

cricket=pd.read_csv('Data/cricket_matches.csv')
cricket_host=cricket[cricket['home'] == cricket['winner']]

team=[]
run_avg=[]
for team_name in cricket_host.home.unique():
    score_inn1=(cricket_host[(cricket_host['innings1'] == team_name) & (np.isnan(cricket_host['win_by_runs']) == ast.literal_eval('False'))]['innings1_runs'])
    score_inn2=cricket_host[(cricket_host['innings2'] == team_name) & (np.isnan(cricket_host['win_by_wickets']) == ast.literal_eval('False'))]['innings2_runs']
    score=(score_inn1.sum()+score_inn2.sum())/(score_inn1.count()+score_inn2.count())
    team.append(team_name)
    run_avg.append(round(score))
home_score=pd.DataFrame({'Home':team,'Score':run_avg})
#remove score with nan
home_score=home_score.dropna()
home_score.to_csv('CSV/Q3_P1.csv')
print(home_score.head())