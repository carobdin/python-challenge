import os
import csv
import pandas as pd

print("Financial Analysis")
print("-------------------------")

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

with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
        
    profit_losses = [int(row['Profit/Losses']) for row in csvreader]

    changes = [profit_losses[i] - profit_losses[i-1] for i in range(1, len(profit_losses))]
    changes_df = pd.DataFrame(changes)

    average = changes_df.mean().values[0]

print(f"Average Change: ${average:.2f}")

# Calculate the greatest increase in profits (date and amount) over the entire period

with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
        
    budget_data = list(csvreader)

    max_increase = 0
    max_increase_date = ""

    for i in range(1, len(budget_data)):
        increase = int(budget_data[i]['Profit/Losses']) - int(budget_data[i-1]['Profit/Losses'])
        if increase > max_increase:
            max_increase = increase
            max_increase_date = budget_data[i]['Date']

print("Greatest increase in profits:", max_increase_date, f"(${max_increase})")

# Calculate the greatest decrease in profits (date and amount) over the entire period

with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
        
    budget_data = list(csvreader)

    min_decrease = float('inf')
    min_decrease_date = ""

    for i in range(1, len(budget_data)):
        decrease = int(budget_data[i]['Profit/Losses']) - int(budget_data[i-1]['Profit/Losses'])
        if decrease < min_decrease:
            min_decrease = decrease
            min_decrease_date = budget_data[i]['Date']

print("Greatest decrease in profits:", min_decrease_date, f"(${min_decrease})")