import pandas as pd
import csv,ast


vehicle= pd.read_csv('Data/vehicle_collisions.csv')

with open('CSV/Q1_P2.csv','w') as csvfile:
    fieldnames = ['BOROUGH','ONE_VEHICLE_INVOLVED','TWO_VEHICLE_INVOLVED','THREE_VEHICLE_INVOVLED','MORE_VEHICLES_INVOLVED']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for borough in(vehicle[~vehicle['BOROUGH'].isnull()]['BOROUGH'].unique()):
        queens=vehicle[vehicle['BOROUGH'] == borough]
        abc=pd.isnull(queens)
        one_vehicle=((abc['VEHICLE 1 TYPE'] == ast.literal_eval('False')) & (abc['VEHICLE 2 TYPE'] == ast.literal_eval('True')) & (abc['VEHICLE 3 TYPE'] == ast.literal_eval('True')) & (abc['VEHICLE 4 TYPE'] == ast.literal_eval('True')) & (abc['VEHICLE 5 TYPE'] == ast.literal_eval('True'))).sum()
        two_vehicle=((abc['VEHICLE 1 TYPE'] == ast.literal_eval('False')) & (abc['VEHICLE 2 TYPE'] == ast.literal_eval('False')) & (abc['VEHICLE 3 TYPE'] == ast.literal_eval('True')) & (abc['VEHICLE 4 TYPE'] == ast.literal_eval('True')) & (abc['VEHICLE 5 TYPE'] == ast.literal_eval('True'))).sum()
        three_vehicle=((abc['VEHICLE 1 TYPE'] == ast.literal_eval('False')) & (abc['VEHICLE 2 TYPE'] == ast.literal_eval('False')) & (abc['VEHICLE 3 TYPE'] == ast.literal_eval('False')) & (abc['VEHICLE 4 TYPE'] == ast.literal_eval('True')) & (abc['VEHICLE 5 TYPE'] == ast.literal_eval('True'))).sum()
    #     four_vehicle=((abc['VEHICLE 1 TYPE'] == ast.literal_eval('False')) & (abc['VEHICLE 2 TYPE'] == ast.literal_eval('False')) & (abc['VEHICLE 3 TYPE'] == ast.literal_eval('False')) & (abc['VEHICLE 4 TYPE'] == ast.literal_eval('False'))& (abc['VEHICLE 5 TYPE'] == ast.literal_eval('True'))).sum()
    #     five_vehicle=((abc['VEHICLE 1 TYPE'] == ast.literal_eval('False')) & (abc['VEHICLE 2 TYPE'] == ast.literal_eval('False')) & (abc['VEHICLE 3 TYPE'] == ast.literal_eval('False')) & (abc['VEHICLE 4 TYPE'] == ast.literal_eval('False')) & (abc['VEHICLE 5 TYPE'] == ast.literal_eval('False'))).sum()
        more_vehicle=len(abc)-one_vehicle-two_vehicle-three_vehicle
        print(borough,one_vehicle,two_vehicle,three_vehicle,more_vehicle)
        writer.writerow({'BOROUGH':borough,'ONE_VEHICLE_INVOLVED':one_vehicle,'TWO_VEHICLE_INVOLVED':two_vehicle,'THREE_VEHICLE_INVOVLED':three_vehicle,'MORE_VEHICLES_INVOLVED':more_vehicle})
    