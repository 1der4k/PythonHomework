# Import modules
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# define function
def votes_analysis(row):
    votes = []

    cand_list = []

    khan_vote = []
    correy_vote = []
    li_vote = []
    otooley_vote = []
      
    # The total number of votes cast
    vote = row[0]
    votes.append(vote)

    # A complete list of candidates who received votes  
    cand_vote = row[2] 
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
    khan_percent = int(sum(khan_vote))/int(len(khan_vote)) * 100
    correy_percent = int(sum(correy_vote))/int(len(correy_vote)) * 100
    li_percent = int(sum(li_vote))/int(len(li_vote)) * 100
    otooley_percent = int(sum(otooley_vote))/int(len(otooley_vote)) * 100

    # The winner of the election based on popular vote.
    cand_vote_totals = [sum(khan_vote,sum(correy_vote,sum(li_vote,sum(otooley_vote))))]
    winner = max(cand_vote_totals)

    # Print to terminal
    print("Election Results")
    print("-------------------------------------------")
    print("Total Votes: " + str(len(votes)))
    print("-------------------------------------------")
    print("Khan: " + str(round(khan_percent, 3)) + " (" + vstr(otes.count("Khan")) +")")
    print("Correy: " + str(round(correy_percent, 3)) + " (" + str(votes.count("Correy")) +")")
    print("Li: " + str(round(li_percent, 3)) + " (" + str(votes.count("Li")) +")")
    print("O'Tooley: " + str(round(otooley_percent, 3)) + " (" + str(votes.count("O'Tooley")) +")")
    print("-------------------------------------------")
    print("Winner: " + winner)

# read in csv file
with open(csvpath, 'r') as csvfile:
    
    header = next(csvfile)

    csvreader = csv.reader(csvfile, delimiter=',')

# Analysis
    for row in csvreader:
        votes_analysis(row)

       


        
        
 

        



# Print to terminal
#print("Election Results")
#print("-------------------------------------------")
#print("Total Votes: " + str(len(votes)))
#print("-------------------------------------------")
#print(cand_list[:])

# Export to text file