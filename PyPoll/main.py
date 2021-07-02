"""PyPoll Homework Solution."""

#Import the required packages
import os
import csv
import statistics

 # Set path for file
csvpath = os.path.join("election.csv")

# Open the CSV
csvfile =  open(csvpath)
csvreader = csv.reader(csvfile, delimiter=",")