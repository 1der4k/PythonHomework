# import modules
import os
import csv


# read in csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    
# analysis and print to terminal
# The total number of months included in the dataset; sum of values in first column

# The net total amount of "Profit/Losses" over the entire period; sum of values in second column

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes; loop through second column capaturing changes in profit/loss, sum, then divide by total number of changes; assign to new column(?)

# The greatest increase in profits (date and amount) over the entire period; find max value in changes of profit/loss column

# The greatest decrease in losses (date and amount) over the entire period; find min value in changes of profit/loss column


# export text file with results