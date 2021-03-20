# Import modules
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# define function
def election_analysis(data):
    total_votes = []

    votes = []

    cand_list = []

    cand_votes = []

    vote_percent = []

    for row in data:  
    # The total number of votes cast
        vote = row[0]
        total_votes.append(vote)
        votes.append(row[2])

        # A complete list of candidates who received votes  
        cand_vote = row[2] 
        if cand_vote not in cand_list:
            cand_list.append(cand_vote)

    # The total number of votes each candidate won
    for candidate in cand_list:
        cand_votes.append(votes.count(candidate))   
    
    # The percentage of votes each candidate won
        vote_percent.append(votes.count(candidate)/int(len(votes)) * 100)

    # The winner of the election based on popular vote.
    winner = cand_list[cand_votes.index(max(cand_votes))]

    # Print to terminal
    print("Election Results")
    print("-------------------------------------------")
    print("Total Votes: " + str(len(votes)))
    print("-------------------------------------------")
    for i in range(len(cand_list)):
        print(f'{cand_list[i]}: {round(vote_percent[i],3)}% ({cand_votes[i]})')
    print("-------------------------------------------")
    print(f'Winner: {winner}')
    print("-------------------------------------------")

    # Export to file
    output_path = os.path.join("Analysis", "election_analysis.txt")

    with open(output_path, 'w', newline='') as txtfile:
        txtfile.write("Election Results")
        txtfile.write("\n-------------------------------------------")
        txtfile.write("\nTotal Votes: " + str(len(votes)))
        txtfile.write("\n-------------------------------------------")
        for i in range(len(cand_list)):
            txtfile.write(f'\n{cand_list[i]}: {round(vote_percent[i],3)}% ({cand_votes[i]})')
        txtfile.write("\n-------------------------------------------")
        txtfile.write(f'\nWinner: {winner}')
        txtfile.write("\n-------------------------------------------")

# read in csv file
with open(csvpath, 'r') as csvfile:
    
    header = next(csvfile)

    csvreader = csv.reader(csvfile, delimiter=',')

# Analysis
    election_analysis(csvreader)