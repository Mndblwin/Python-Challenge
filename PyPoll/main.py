"""PyPoll Homework Solution."""

#Import the required packages
import os
import csv
import statistics
from typing import Counter

 # Set input/output path for file
csvpath = os.path.join("PyPoll", "election_data.csv")
outfile = os.path.join("PyPoll", "Analysis", "PyPoll_analysis.txt")

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

print(f"Election Results\n"
    f"--------------------------------")

print(f"Total Votes: {len(voter_id)}")

print(f"--------------------------------")
candidate_Khan = candidate.count('Khan')
percent_Khan = (candidate.count('Khan') / (len(voter_id)) * 100)
round_Khan = round(percent_Khan, 2)
print(f"Khan: {round_Khan}{candidate_Khan}")

candidate_Correy = candidate.count('Correy')
percent_Correy = (candidate.count('Correy') / (len(voter_id)) * 100)
round_Correy = round(percent_Correy, 2)
print(f"Correy: {round_Correy} {candidate_Correy}")

candidate_Li = candidate.count('Li')
percent_Li = (candidate.count('Li') / (len(voter_id)) * 100)
round_Li = round(percent_Correy, 2)
print(f"Li: {round_Li} {candidate_Li}")

candidate_OTooley = candidate.count("O'Tooley")
percent_OTooley = (candidate.count("O'Tooley") / (len(voter_id)) * 100)
round_OTooley = round(percent_OTooley, 2)
print(f"OTooley: {round_OTooley} {candidate_OTooley}")

print(f"--------------------------------")

def winner (candidate):
    return max(set(candidate), key = candidate.count)
print(f'Winner:' + str(winner(candidate)))

# create output file 
with open(outfile, 'w') as textfile:
    textfile.write(f"Election Results\n"
                f"--------------------------------\n"
                f"Total Votes: {len(voter_id)}\n"
                f"--------------------------------\n")

    textfile.write(f"Khan: {round_Khan} {candidate_Khan}\n"
                f"Correy: {round_Correy} {candidate_Correy}\n"
                f"Li: {round_Li} {candidate_Li}\n"
                f"OTooley: {round_OTooley} {candidate_OTooley}\n"
                f"--------------------------------\n")
    textfile.write(f'Winner:' + str(winner(candidate)))
                