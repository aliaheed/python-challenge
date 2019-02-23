# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'election_data.csv')

#  initializing variables and lists
total_votes = 0
count_individual_votes = 0

list_candidates = []
election_candidate_vote = []
candidate = []
votes = []
percentage = []
final_list = []

winner = ''
popular_vote = 0

#  reading csv file and storing in list and storing unique candidates name in a list.
#  also counting total votes casted in the election
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row without any other operation
    next (csvreader,None)

    for row in csvreader:
        election_candidate_vote.append(row[2])
        if row[2] not in list_candidates:
            list_candidates.append(row[2])

        total_votes = total_votes + 1

#  looping for each unique candidate and create a final list to store
#  candidate name, votes casted for individual candidate and the percentage of votes
#  for each candidate
for i in range(len(list_candidates)):
    final_list.append(list_candidates[i])
    for j in range(len(election_candidate_vote)):
        if list_candidates[i] == election_candidate_vote[j]:
            count_individual_votes = count_individual_votes + 1
    final_list.append(count_individual_votes)
    final_list.append(round(count_individual_votes/total_votes*100,3))
    count_individual_votes=0

#  storing candidates, their votes casted and percentage in specific lists
#  for easier printing
for i, final in enumerate(final_list, 1):
    if i % 3 == 1:
        candidate.append(final_list[i-1])

    if i % 3 == 2:
        votes.append(final_list[i-1])
    
        if final_list[i-1] > popular_vote:
            popular_vote = final_list[i-1]
            winner = final_list[i-2]

    if i % 3 == 0:
        percentage.append(final_list[i-1])

#  printing output to terminal
print("Election Results")
print("-------------------------------")
print(f'Total Votes: {total_votes}')
print("-------------------------------")
for i in range(len(candidate)):
    print(f'{candidate[i]}: {"{}%".format(percentage[i])} ({votes[i]})' )
print("-------------------------------")
print(f'Winner: {winner}')
print("-------------------------------")

# printing output to file
# Set variable for output file
output_file = os.path.join("output_election_data.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Election Results"])
    writer.writerow(["------------------------------"])
    writer.writerow([f"Total Votes: {total_votes}"])
    for i in range(len(candidate)):
        writer.writerow([f'{candidate[i]}: {"{}%".format(percentage[i])} ({votes[i]})'])
    writer.writerow(["------------------------------"])
    writer.writerow([f"Winner: {winner}"])
    writer.writerow(["------------------------------"])
