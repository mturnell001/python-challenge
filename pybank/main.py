import os
import csv
import pandas as pd

#read in budget data to pandas df
csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')
budget_df = pd.read_csv(csvpath)

#number of rows is the number of months
months = len(budget_df)

#slice off the profit column for ease of use
profit = budget_df['Profit/Losses']

totalProfit = 0.0
#sum column 2, store in totalProfit
for i in profit:
    totalProfit += i

avgProfit = totalProfit / months #average = sum / number of entries

#return the rows where the max profit and max loss are located in the df
maxProfit = (budget_df.loc[budget_df['Profit/Losses'] == max(profit)]).values[0]
maxLoss = (budget_df.loc[budget_df['Profit/Losses'] == min(profit)]).values[0]

#output analysis to terminal
print("Financial Analysis \n -------------------------\n")
print("Total Months: " + str(months))
print("Total: " + str(totalProfit))
print("Average Change: " + str(avgProfit))
print("Greatest Increase in Profits: " + str(maxProfit))
print("Greatest Decrease in Profits: " + str(maxLoss))

#create output .txt and write to it
outfile = open("output.txt","w")   
 
outfile.write("Financial Analysis \n -------------------------\n")
outfile.write("Total Months: " + str(months))
outfile.write("\nTotal: " + str(totalProfit))
outfile.write("\nAverage Change: " + str(avgProfit))
outfile.write("\nGreatest Increase in Profits: " + str(maxProfit))
outfile.write("\nGreatest Decrease in Profits: " + str(maxLoss)) 
outfile.close()  



    