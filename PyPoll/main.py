"""PyPoll Homework Solution."""

#Import the required packages
import os
import csv
import statistics

 # Set path for file
csvpath = os.path.join("PyPoll", "election_data.csv")

# Open the CSV
csvfile =  open(csvpath)
csvreader = csv.reader(csvfile, delimiter=",")

# My variables to hold the list of election
voter_id = []
county = []
candidate = []
