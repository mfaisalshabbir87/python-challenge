import os
import csv

#choose file
file_num = 1

# Identifies file with poll data
file = os.path.join('raw_data', 'election_data_' + str(file_num) + '.csv')

#candidate name and vote count dictionary.
poll = {}

#set total votes to zero.
total_votes = 0

#read data file
with open(file, 'r') as csvfile:
    csvread = csv.reader(csvfile)

    next(csvread, None)

    #creates dictionary from file using column 3 as keys, using each name only once.

    for row in csvread:
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1

#create empty list for candidates and  vote count
candidates = []
num_votes = []

#takes dictionary keys and values and store in lists

for key, value in poll.items():
    candidates.append(key)
    num_votes.append(value)


vote_percent = []
for n in num_votes:
    vote_percent.append(round(n/total_votes*100, 1))

# combine candidates, num_votes, vote_percent into tuples
clean_data = list(zip(candidates, num_votes, vote_percent))

#create winner_list
winner_list = []

for name in clean_data:
    if max(num_votes) == name[1]:
        winner_list.append(name[0])


winner = winner_list[0]

if len(winner_list) > 1:
    for w in range(1, len(winner_list)):
        winner = winner + ", " + winner_list[w]

#prints to file
output_path = os.path.join('Output', 'election_results_' + str(file_num) +'.txt')

with open(output_path, 'w') as txtfile:
    txtfile.writelines('Election Results \n------- \nTotal Votes: ' + str(total_votes) +
      '\n-------\n')
    for entry in clean_data:
        txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txtfile.writelines('------- \nWinner: ' + winner + '\n-------')

#prints file to terminal
with open(output_path, 'r') as readfile:
    print(readfile.read())
