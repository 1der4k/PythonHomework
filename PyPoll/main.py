# Import modules
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# define function
def votes_analysis(data):
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
    # if cand_vote == "Khan":
    #     khan_vote.append(cand_vote)
    # elif cand_vote == "Correy":
    #     correy_vote.append(cand_vote)
    # elif cand_vote == "Li":
    #     li_vote.append(cand_vote)
    # elif cand_vote == "O'Tooley":
    #     otooley_vote.append(cand_vote)

    # The percentage of votes each candidate won
        vote_percent.append(votes.count(candidate)/int(len(votes)) * 100)
    # khan_percent = int(len(khan_vote))/len(votes) * 100
    # correy_percent = int(len(correy_vote))/len(votes) * 100
    # li_percent = int(len(li_vote))/len(votes)  * 100
    # otooley_percent = int(len(otooley_vote))/len(votes)  * 100

    # The winner of the election based on popular vote.
    winner = cand_list[cand_votes.index(max(cand_votes))]
    # cand_vote_totals = [int(len(khan_vote)),int(len(correy_vote)),int(len(li_vote)),int(len(otooley_vote))]
    # winner = cand_list[cand_vote_totals.index(max(cand_vote_totals))]

    # Print to terminal
    print("Election Results")
    print("-------------------------------------------")
    print("Total Votes: " + str(len(votes)))
    print("-------------------------------------------")
    for i in range(len(cand_list)):
        print(f'{cand_list[i]}: {round(vote_percent[i],3)}% ({cand_votes[i]})')
    # print("Khan: " + str(round(khan_percent,3)) + "%" + " (" + str(khan_vote.count("Khan")) +")")
    # print("Correy: " + str(round(correy_percent,3)) + "%"  + " (" + str(correy_vote.count("Correy")) +")")
    # print("Li: " + str(round(li_percent,3)) + "%"  + " (" + str(li_vote.count("Li")) +")")
    # print("O'Tooley: " + str(round(otooley_percent,3)) + "%"  + " (" + str(otooley_vote.count("O'Tooley")) +")")
    print("-------------------------------------------")
    print(f'Winner: {winner}')
    print("-------------------------------------------")

# read in csv file
with open(csvpath, 'r') as csvfile:
    
    header = next(csvfile)

    csvreader = csv.reader(csvfile, delimiter=',')

# Analysis
    votes_analysis(csvreader)

       


        
        
 

        



# Print to terminal
#print("Election Results")
#print("-------------------------------------------")
#print("Total Votes: " + str(len(votes)))
#print("-------------------------------------------")
#print(cand_list[:])

# Export to text file