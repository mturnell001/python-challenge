import os
import csv
import pandas as pd


#read in election data to pandas df
csvpath = os.path.join('..', 'PyPoll', 'election_data.csv')
vote_df = pd.read_csv(csvpath)

#number of rows = number of votes
numVotes = len(vote_df)

#slice off candidates column for ease of use
candidates = vote_df['Candidate']

#gives list of candidate choices
choices = candidates.unique().tolist()

#gives number of votes per candidate in same order as choices
voteCT = candidates.value_counts().to_list()
votePCT = candidates.value_counts(normalize=True).to_list()

#format the ratio of votes to a percentage
votePCT = [round((i * 100),2) for i in votePCT]

#determine the winning candidate based on vote count
wincount = 0
for i in range(len(voteCT)):
    if voteCT[i] > wincount:
        winner = choices[i]
        wincount = voteCT[i]
        
#output election analysis to terminal
print("Election Results")
print("---------------------")
print("Total Votes: " + str(numVotes))
print("---------------------")
for i in range(len(choices)):
    print(choices[i] + ': ' + str(votePCT[i]) + '% (' + str(voteCT[i]) + ')')
print("---------------------")
print("Winner: " + winner)
print("---------------------")

#create output .txt and write to it
outfile = open("output.txt","w")

outfile.write("Election Results\n")
outfile.write("---------------------\n")
outfile.write("Total Votes: " + str(numVotes))
outfile.write("\n---------------------\n")
for i in range(len(choices)):
    outfile.write(choices[i] + ': ' + str(votePCT[i]) + '% (' + str(voteCT[i]) + ')\n')
outfile.write("---------------------\n")
outfile.write("Winner: " + winner)
outfile.write("\n---------------------")
outfile.close()