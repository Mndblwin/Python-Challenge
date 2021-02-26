import os
import csv

csvpath = os.path.join('..','PyBank','Resources','Budget_data.csv')
print(csvpath)

# 'Open' the csv file and use csv.reader to allow 
csvfile = open(csvpath)

# csv.reader creates an object called an *iterator* that allows us to iterate over the rows using a for loop
csvreader = csv.reader(csvfile, delimiter=',')

# Print each row of data in the csv file
#for row in csvreader:
 #print(row)

 # Read through each row of data after the header
    for row in csv_reader:

        