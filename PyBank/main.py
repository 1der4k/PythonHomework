# import modules
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# define function
#def analysis(row):
    



    

    # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes; loop through second column capaturing changes in profit/loss, sum, then divide by total number of changes; assign to new column(?)

    

# read in csv file
with open(csvpath, 'r') as csvfile:
    
    header = next(csvfile)

    csvreader = csv.reader(csvfile, delimiter=',')

    total_months = []
    profits_losses = []
    changes_profits_losses =[]


    for row in csvreader:
        
        # The total number of months included in the dataset; total number of entries in first column
        month = row[0]
        total_months.append(month)
        
        # The net total amount of "Profit/Losses" over the entire period; sum of values in second column
        profit_loss = row[1]
        profits_losses.append(int(profit_loss))

        # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
        # I had some intuition about this, but the solution on this page clarified it for me: https://stackoverflow.com/questions/46965192/python-how-can-i-find-difference-between-two-rows-of-same-column-using-loop-in. However, when I initially attempted to run the code, I did not
        # get a reasonable number as a result. Looking at my reference, it seemed like my problem was that I had placed this loop in the csvreader loop. I wasn't sure why this was a problem, at first, but after some thought I realized that none of the variables that the i loop
        # was referencing were actually in rows in the reader, so placing it in there was unnecessary and was causing the i loop to over-iterate. Additionally, this helped illustrate to me the process that is actually happening when a loop goes through a reader.
        
    for i in range(1,len(profits_losses)):
        changes_profits_losses.append(profits_losses[i] - profits_losses[i-1])
        avg_changes_profits_losses = sum(changes_profits_losses)/len(changes_profits_losses)

        # The greatest increase in profits (date and amount) over the entire period; find max value in changes of profit/loss column

        # The greatest decrease in losses (date and amount) over the entire period; find min value in changes of profit/loss column
    

# Print to terminal
print("Financial Analysis")
print("--------------------------------------------------")
#print(len(total_months))
print("Total Months: " + str(len(total_months)))
print(sum(profits_losses))
print(avg_changes_profits_losses)
print(max(changes_profits_losses))
print(min(changes_profits_losses))


# Export to file