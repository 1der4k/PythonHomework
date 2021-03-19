# Import modules
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# read in csv file
with open(csvpath, 'r') as csvfile:
    
    header = next(csvfile)

    csvreader = csv.reader(csvfile, delimiter=',')

# Analysis
    votes = []
    cand_list = []

    for row in csvreader:
# The total number of votes cast
        vote = row[0]
        votes.append(vote)

# A complete list of candidates who received votes
        candidate = row[2]
        if candidate not in cand_list:
            cand_list.append(candidate)
        
# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.


# Print to terminal
print("Election Results")
print("-------------------------------------------")
print("Total Votes: " + str(len(votes)))
print("-------------------------------------------")
print(cand_list[:])

# Export to text file