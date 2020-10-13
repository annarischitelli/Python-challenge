import os
import csv

# Set path for file
election_data = os.path.join("PyPoll", "Resources", "election_data.csv")

# Set variable value
vote_count = []
total_votes = 0
candidates = {}
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
        # candidates = (row[2])
        # if candidates in individual_candidate:
        #     candidate_index = individual_candidate.index (candidates)
        #     vote_count[candidate_index] = vote_count[candidate_index] + 1
        # else:
        #     # if candidate not found
        #     individual_candidate.append(candidates)
        #     vote_count.append(1)
        if candidates.get(row[2]):
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

winning_candidate = ""
highest_votes = 0

for candidate_name, candidate_votes in candidates.items():
    print(candidate_name, candidate_votes)
    print(candidate_name, (candidate_votes/float(total_votes))*100)

    if candidate_votes > highest_votes:
        winning_candidate = candidate_name
        highest_votes = candidate_votes
print(winning_candidate)


# # Test list so far
# print(f"total_votes {total_votes}")
# print(f"For candidate: {individual_candidate}")
# print(f"Index: {individual_candidate.index(candidates)}")

# percent_total_votes = []
# greatest_votes = vote_count[0]
# greatest_index = 0

# for x in range(len(individual_candidate)):
#     percent_total_votes_V2 = round(vote_count[x]/total_votes*100,2)
#     percent_total_votes.append(percent_total_votes_V2)

#     if vote_count[x] > greatest_votes:
#         greatest_votes = vote_count[x]
#         greatest_index = x

#     winner = individual_candidate[greatest_index]

# # Show all information
# print("Election Results")
# print("----------------")
# print(f"Total Votes: {vote_count}")
# print("----------------")
# for x in range (len(candidates)):
#     print(f"{candidates[x]}: {percent_total_votes_V2[x]}% ({total_votes[x]}")
# print("----------------")
# print("Winner: {winner}")
# print("----------------")

# # Output as txt file
# output_file = os.path.join("pybank_results.txt")
# with open(output_file, "w", newline="") as datafile:
#     datafile.write("Election Results")
#     datafile.write("----------------")
#     datafile.write(f"Total Votes: {vote_count}")
#     datafile.write("----------------")
#     for count in range (len(candidates)):
#         datafile.write(f"{candidates[x]}: {percent_total_votes_V2[x]}% ({total_votes[x]})")
#     datafile.write("----------------")
#     datafile.write("Winner: {winner}")
#     datafile.write("----------------")

    