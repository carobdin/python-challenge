import os
import csv
import pandas as pd

print("Election Results")
print("-------------------------")

csvpath = os.path.join("Resources", "election_data.csv")

# Calculate the total number of votes cast

with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile)

    header = next(csvreader)

    total_votes = sum(1 for row in csvreader)
    
print("Total Votes:", total_votes)
print("-------------------------")

# Calculate the percentage of votes each candidate won

with open(csvpath, encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile)

        candidate_counts = {}

        total_votes = 0
        for row in csvreader:
            total_votes += 1
            candidate = row["Candidate"]
            if candidate not in candidate_counts:
                candidate_counts[candidate] = 1
            else:
                candidate_counts[candidate] += 1


for candidate, count in candidate_counts.items():
        percentage = (count / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({count} votes)")
print("-------------------------")

# Find the winner of the election based on popular vote

winner = max(candidate_counts, key=candidate_counts.get)

print(f"Winner: {winner}")
print("-------------------------")
