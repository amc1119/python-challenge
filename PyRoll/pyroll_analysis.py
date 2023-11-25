# Allow file paths to be created across operating systems
import os
import string

# Module for reading CSV files
import csv

poll_csv = os.path.join('Resources', 'election_data.csv')
analysis_path = "Analysis/final_analysis.txt"

with open(poll_csv, 'r') as poll_file:
    
    total_votes_cast = 0
    candidates_with_votes = {}
    percentage_of_votes = 0
    total_votes = 0
    candidate_counter = 0
    results_list = []

    # CSV reader specifies delimiter and "data" holds the contents
    poll_csvreader = csv.reader(poll_file, delimiter=',')

    # Read the header row first
    data_header = next(poll_csvreader)

    # Read each row of data after the header
    for row in poll_csvreader:
        total_votes_cast = total_votes_cast + 1
        name = row[2]

        if name not in candidates_with_votes:
            candidates_with_votes[name] = 1 
            candidates = list(candidates_with_votes.keys())
            candidate_counter += 1
        else:
            candidates_with_votes[name] += 1
            votes_per_candidate = list(candidates_with_votes.values())
            # winner = (max(votes_per_candidate)).index()

for i in range(len(votes_per_candidate)):
    percentage_of_votes = (votes_per_candidate[i])/total_votes_cast * 100
    results = (f"{candidates[i]}: {round(percentage_of_votes, 3)}% ({votes_per_candidate[i]})")
    results_list.append(results)
    
most_votes = max(votes_per_candidate)
winner = votes_per_candidate.index(most_votes)

output = f"""
Election Results
-------------------------
Total Votes: {total_votes_cast}
-------------------------
{chr(10).join(results_list)}
-------------------------
Winner: {candidates[winner]}
-------------------------
"""

print(output)

with open(analysis_path, "w") as output_file:
    output_file.write(output)