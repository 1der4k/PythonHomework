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
    candidates = set()
    #cand_set = set(candidates)
    cand_list = []

    for row in csvreader:
# The total number of votes cast
        vote = row[0]
        votes.append(vote)

# A complete list of candidates who received votes
        candidate = row[2]
        candidates.add(candidate)
        
# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.


# Print to terminal
print("Election Results")
print("-------------------------------------------")
print("Total Votes: " + str(len(votes)))
print("-------------------------------------------")
for x in candidates:
    cand_list.append(x)
print(cand_list[:])

# Export to text file