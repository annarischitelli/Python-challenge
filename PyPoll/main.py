import os
import csv

# Set path for file
election_data = os.path.join("PyPoll", "Resources", "election_data.csv")

# Set variable value
vote_count = []
total_votes = 0
candidates = []
individual_candidate = []
percent_total_votes = []

# Read csv and add to sscript
with open (election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Header row
    csv_header = next(csvreader)

    # Read first row + count votes
    for row in csvreader:
        vote_count = vote_count + 1
        # Identify list of candidates
        candidate = row[2]
        candidates.append(row[2])
    # Create list of individual candidates
    for i in set(candidates):
        individual_candidate.append(i)
        votes_per_candidate = candidates.count(i)
        vote_count.append(votes_per_candidate)
        percent_per_candidate = (votes_per_candidate/count)*100
        percent_total_votes.append(percent_per_candidate)

    winner_count = max(vote_count)
    winner = individual_candidate[vote_count.index(winner_count)]

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