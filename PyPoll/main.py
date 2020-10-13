import os
import csv

# Set path for file
election_data = os.path.join("PyPoll", "Resources", "election_data.csv")

# Set variable value
vote_count = []
total_votes = 0
candidates = []
individual_candidate = []

# Read csv and add to script
with open (election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    # Header row
    csv_header = next(csvreader)

    # Read first row + count votes
    for row in csvreader:
        # Add each vote (row) to total votes
        total_votes += 1
        # Identify candidate in row + add to list (if found)
        candidates = (row[2])
        if candidates in individual_candidate:
            candidate_index = individual_candidate.index (candidates)
            vote_count[candidate_index] = vote_count[candidate_index] + 1
        else:
            # if candidate not found
            individual_candidate.append(candidates)
            vote_count.append(1)

# # Test list so far
# print(f"total_votes {total_votes}")
# print(f"For candidate: {individual_candidate}")
# print(f"Index: {individual_candidate.index(candidates)}")

percent_total_votes = []
greatest_votes = vote_count[0]
greatest_index = 0

for x in range(len(individual_candidate)):
    percent_total_votes_V2 = round(vote_count[x]/total_votes*100,2)
    percent_total_votes.append(percent_total_votes_V2)

    if vote_count[x] > greatest_votes:
        greatest_votes = vote_count[x]
        greatest_index = x

    winner = individual_candidate[greatest_index]

# Show all information
print("Election Results")
print("----------------")
print(f"Total Votes: {str(vote_count)}")
print("----------------")
for count in range (len(candidates)):
    print(f"{candidate(count)}: {percent_per_candidate[count]}% ({total_votes[count]})")
print("----------------")
print("Winner: {winner}")
print("----------------")