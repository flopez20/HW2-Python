from pathlib import Path
print(f"Current Working Directory: {Path.cwd()}")

import csv

csvpath = Path('budget_data.csv')

profit_losses = []

line_num = 0

with open(csvpath, 'r') as csvfile:


    print(type(csvfile))
    
    csvreader = csv.reader(csvfile, delimiter=',')

    print(type(csvreader))
    
    header = next(csvreader)
    line_num += 1
  
    print(f"{header} <---- HEADER")
    
    for row in csvreader:
        # Print the row
        print(row)
        # Set profit_loss variable equal to the value in the 2nd column of each row
        profit_loss = int(row[1])
        # Append the row salary value to the list of salaries
        profit_losses.append(profit_loss)
        
# Initialize metric variables
total_months = 0
total_net_profit_losses = 0
avg_changes_profit_losses = 0
greatest_increase = 0
greatest_decrease = 0


# Calculate the max, minn, and average of the list of profit/losses
for profit_loss in profit_losses:
    # Sum the total and count variables
    total_net_profit_losses += profit_loss
    total_months += 1

total_months
total_net_profit_losses



