import os
import csv
import pandas as pd

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile)

    header = next(csvreader)

# Calculate the total number of months included in the dataset

    total_months = sum(1 for row in csvreader)
    
print("Total months:", total_months)

# Calculate the net total amount of "Profit/Losses" over the entire period

with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile)

    header = next(csvreader)
    net_total = 0
    for row in csvreader:
        net_total += int(row[1])
    
print("Total: $", net_total)


# Calculate the changes in "Profit/Losses" over the entire period, and then the average of those changes

budget_data = pd.read_csv(csvpath)

changes = [budget_data["Profit/Losses"][i] - budget_data["Profit/Losses"][i-1] for i in range(1, len(budget_data["Profit/Losses"]))]
changes_df = pd.DataFrame(changes)

average = changes_df.mean()

print("Average Change: $", average)

# Calculate the greatest increase in profits (date and amount) over the entire period

budget_data = pd.read_csv(csvpath)

max_increase = 0
max_increase_date = ""

for i in range(1, len(budget_data["Profit/Losses"])):
        increase = budget_data["Profit/Losses"][i] - budget_data["Profit/Losses"][i-1]
        if increase > max_increase:
            max_increase = increase
            max_increase_date = budget_data["Date"][i]

print("Greatest increase in profits:", max_increase_date, "($", max_increase, ")")

# Calculate the greatest decrease in profits (date and amount) over the entire period

budget_data = pd.read_csv(csvpath)

min_decrease = float('inf')
min_decrease_date = ""

for i in range(1, len(budget_data["Profit/Losses"])):
        decrease = budget_data["Profit/Losses"][i] - budget_data["Profit/Losses"][i-1]
        if decrease < min_decrease:
            min_decrease = decrease
            min_decrease_date = budget_data["Date"][i]

print("Greatest decrease in profits:", min_decrease_date, "($", min_decrease, ")")