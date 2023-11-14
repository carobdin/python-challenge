# python-challenge

This project consists of two parts: a financial analysis and an election results analysis, implemented using Python language.

## Financial Analysis
### Overview
The financial analysis involves examining the budget_data.csv file. It calculates and analyzes various financial metrics over a specific period.

### Metrics Calculated
1. Total Months: Calculates the total number of months included in the dataset.
2. Net Total Profit/Losses: Calculates the total amount of "Profit/Losses" over the entire period.
3. Changes in Profit/Losses: Calculates the changes in "Profit/Losses" over the entire period and then calculates the average of those changes.
4. Greatest Increase in Profits: Identifies the date and amount of the greatest increase in profits over the entire period.
5. Greatest Decrease in Profits: Identifies the date and amount of the greatest decrease in profits over the entire period.

### Execution on Terminal
To run the financial analysis, execute the Python script in the terminal:

python bank.py

## Election Results Analysis
### Overview
The election results analysis involves examining the election_data.csv file. It analyzes the votes cast and determines the election results based on candidate votes.

### Metrics Calculated
1. Total Votes Cast: Calculates the total number of votes cast.
2. List of Candidates: Provides a complete list of candidates who received votes.
3. Percentage of Votes: Calculates the percentage of votes each candidate won.
4. Total Votes for Each Candidate: Determines the total number of votes each candidate won.
5. Election Winner: Identifies the winner of the election based on the popular vote.

### Execution on Terminal
To run the election results analysis, execute the Python script in the terminal:

python election.py
