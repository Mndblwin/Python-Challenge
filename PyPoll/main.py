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

# My variables to hold the list of election data
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
#print(f"Khan: {sum(candidate.count(['Khan']))}")
#print(candidate.count('Khan'))
candidate_Khan = candidate.count('Khan')
print(f'Khan: '+ str(candidate_Khan))

candidate_Correy = candidate.count('Correy')
print(f'Correy: '+ str(candidate_Correy))

candidate_Li = candidate.count('Li')
print(f'Li: '+ str(candidate_Li))

candidate_OTooley = candidate.count("O'Tooley")
print(f'OTooley: '+ str(candidate_OTooley))
    



