import os
import csv

# Set path for file
election_data = os.path.join("PyPoll", "Resources", "election_data.csv")

# Set variable value
vote_count = 0
total_votes = 0
candidates = {}

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
        if candidates.get(row[2]):
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

winning_candidate = ""
highest_votes = 0

for candidate_name, candidate_votes in candidates.items():
    # Testing to make sure it's working
    # print(candidate_name, candidate_votes)
    # print(candidate_name, (candidate_votes/float(total_votes))*100)
    if candidate_votes > highest_votes:
        winning_candidate = candidate_name
        highest_votes = candidate_votes
print(winning_candidate)

# Show all information
print("Election Results")
print("----------------")
print(f"Total Votes: {total_votes}")
print("----------------")
for candidate_name, candidate_votes in candidates.items():
    print(f"{candidate_name}: {round(candidate_votes/float(total_votes)*100)}% {candidate_votes}")
print("----------------")
print(f"Winner: {winning_candidate}")
print("----------------")

# # Output as txt file
output_file = os.path.join("pypoll_results.txt")
with open(output_file, "w", newline="") as datafile:
    datafile.write("Election Results")
    datafile.write("----------------")
    datafile.write(f"Total Votes: {total_votes}")
    datafile.write("----------------")
    for candidate_name, candidate_votes in candidates.items():
        datafile.write(f"{candidate_name}: {round(candidate_votes/float(total_votes)*100)}% {candidate_votes}")
    datafile.write("----------------")
    datafile.write(f"Winner: {winning_candidate}")
    datafile.write("----------------")

    