#import the neccessory libraries
import csv
import os
csvpath= os.path.join('Resources','budget_data.csv')
#csvpath="../Resources/budget_data.csv"
with open(csvpath)as cvsfile:
    csvreader = csv.reader(cvsfile, delimiter=',')
    print(csvreader)
    budget_data_to_load = "Resources/budget_data.csv"