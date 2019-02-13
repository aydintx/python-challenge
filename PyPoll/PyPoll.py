import os
import csv
filename="election_data.csv"
# Set path for file
csvpath = os.path.join(filename)
with open(csvpath, newline='') as csvfile:

#   CSV reader specifies delimiter and variable that holds contents

    csvreader = csv.reader(csvfile, delimiter=',')
#     print(csvreader)

#    Read the header row first 

    csv_header = next(csvreader)

    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    voters=0
    votes={} # candidates and their votes

    for row in csvreader:
        #print(row)
        voters+=1
        votes.update({row[2]: 0})
        # forms the dictionary with the candidate names and initial vote counts.
with open(csvpath, newline='') as csvfile:
#   CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    for x in votes:
#         print(x)
        for row in csvreader:
            if row[2] in votes:
                votes[row[2]]=votes[row[2]]+1

# Converts dictionary to a list

candidates_votes=[]

temp=[]

for key, value in votes.items():

    temp = [key,value]

    candidates_votes.append(temp)

#print(candidates_votes)

#Sorting the candidate votes descending

candidates_votes.sort(key=lambda x: x[1], reverse=True)

#print(candidates_votes)

print("Election Results")

print("-------------------------")

print(f"Total Votes: {voters}")

print("-------------------------")

for i in range(0,len(candidates_votes)):

     print(f"{candidates_votes[i][0]}: {round(candidates_votes[i][1]*100/voters,3)}% ({candidates_votes[i][1]})")

print("-------------------------")

print(f"Winner: {candidates_votes[0][0]}")
print("-------------------------")