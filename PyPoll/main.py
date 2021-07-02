"""PyPoll Homework Solution."""

#Import the required packages
import os
import csv
import statistics
from typing import Counter

 # Set path for file
csvpath = os.path.join("PyPoll", "election_data.csv")

# Open the CSV
csvfile =  open(csvpath)
csvreader = csv.reader(csvfile, delimiter=",")

# My variables to hold the list of election
voter_id = []
county = []
candidate = []

# Skips header
header = next(csvreader)

for row in csvreader:
    voter_id.append(row[0])
    county.append(row[1])
    candidate.append(row[2])
#print(len('Total Votes: '+ str(voter_id)))
# vote_counts = [int(i) for i in voter_id if i != "NA"]
#vote_counts.count(voter_id)
print(f"Total Votes: {len(voter_id)}")


    



