import os
import csv
import operator

TotalVotes = 0
candidates = {}
winner = ""

csvpath = os.path.join("election_data_1.csv")
with open(csvpath, 'r', encoding='utf-8') as csvfile:
    csvread = csv.reader(csvfile)

    next(csvread, None)

    for row in csvread:
        TotalVotes = TotalVotes + 1
        count = candidates.get(row[2], 0)
        candidates[row[2]] = count + 1


candidates_list = candidates.keys()
winner = max(candidates.items(), key=operator.itemgetter(1))[0]

print("Election Results")
print("----------------------")
print("Total Votes: " + str(TotalVotes))
print("----------------------")
for candidate in candidates_list:
    print(candidate, str(candidates[candidate]), str(100*candidates[candidate]/TotalVotes) + "%")
print("----------------------")
print("Winner: " + winner)
print("----------------------")

with open("C:\Documents\Election.txt", 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("----------------------\n")
    txtfile.write("Total Votes: " + str(TotalVotes) + "\n")
    txtfile.write("----------------------\n")
    for candidate in candidates_list:
        txtfile.write(candidate + " " + str(candidates[candidate]) + " " + str(100 * candidates[candidate] / TotalVotes) + "%\n")
    txtfile.write("----------------------\n")
    txtfile.write("Winner: " + winner + "\n")
    txtfile.write("----------------------\n")
