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

    for row in csvreader:
# The total number of votes cast
        vote = row[0]
        votes.append(vote)

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.


# Print to terminal
print("Election Results")
print("-------------------------------------------")
print("Total Votes: " + str(len(votes)))

# Export to text file
