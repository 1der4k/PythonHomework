# import modules
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# define function
#def analysis(row):
    



    

    # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes; loop through second column capaturing changes in profit/loss, sum, then divide by total number of changes; assign to new column(?)

    # The greatest increase in profits (date and amount) over the entire period; find max value in changes of profit/loss column

    # The greatest decrease in losses (date and amount) over the entire period; find min value in changes of profit/loss column

# read in csv file
with open(csvpath, 'r') as csvfile:
    
    header = next(csvfile)

    csvreader = csv.reader(csvfile, delimiter=',')

    total_months = []
    profits_losses = []



    for row in csvreader:
        
        #date = row[0]
        #prof_loss = row[1]
        #plvalues = []
    
        # The total number of months included in the dataset; total number of entries in first column
        
        month = row[0]
        total_months.append(month)
        
        # The net total amount of "Profit/Losses" over the entire period; sum of values in second column
        p_l = row[1]
        profits_losses.append(int(p_l))

    

# Run analysis
print(len(total_months))
print(sum(profits_losses))


# Print to terminal

# Export to file