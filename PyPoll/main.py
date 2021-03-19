# Import modules
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# define function
def votes_analysis(row):
    votes = []
    vote = row[0]
    cand_list = []
    cand_vote = row[2]

    khan_vote = []
    correy_vote = []
    li_vote = []
    otooley_vote = []

    khan_percent = sum(khan_vote)/len(khan_vote) * 100
    correy_percent = sum(correy_vote)/len(correy_vote) * 100
    li_percent = sum(li_vote)/len(li_vote) * 100
    otooley_percent = sum(otooley_vote)/len(otooley_vote) * 100

    cand_vote_totals = [sum(khan_vote,sum(correy_vote,sum(li_vote,sum(otooley_vote))))]
    winner = max(cand_vote_totals)
    
    # The total number of votes cast
    votes.append(vote)
    # A complete list of candidates who received votes   
    if cand_vote not in cand_list:
            cand_list.append(cand_vote)
    # The total number of votes each candidate won  
    if cand_vote == "Khan":
        khan_vote.append(cand_vote)
    elif cand_vote == "Correy":
        correy_vote.append(cand_vote)
    elif cand_vote == "Li":
        li_vote.append(cand_vote)
    elif cand_vote == "o'Tooley":
        otooley_vote.append(cand_vote)
    # The percentage of votes each candidate won

    # The winner of the election based on popular vote.

    # Print to terminal
    print("Election Results")
    print("-------------------------------------------")
    print("Total Votes: " + str(len(votes)))
    print("-------------------------------------------")
    print("Khan: " + round(khan_percent, 3)) + " (" + votes.count("Khan") +")"
    print("Correy: " + round(correy_percent, 3)) + " (" + votes.count("Correy") +")"
    print("Li: " + round(li_percent, 3)) + " (" + votes.count("Li") +")"
    print("O'Tooley: " + round(otooley_percent, 3)) + " (" + votes.count("O'Tooley") +")"
    print("-------------------------------------------")
    print("Winner: " + winner)

# read in csv file
with open(csvpath, 'r') as csvfile:
    
    header = next(csvfile)

    csvreader = csv.reader(csvfile, delimiter=',')

# Analysis
    for row in csvreader:
        votes_analysis

       


        
        
 

        



# Print to terminal
#print("Election Results")
#print("-------------------------------------------")
#print("Total Votes: " + str(len(votes)))
#print("-------------------------------------------")
#print(cand_list[:])

# Export to text file