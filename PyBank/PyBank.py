from pathlib import Path
print(f"Current Working Directory: {Path.cwd()}")

import csv

csvpath = Path('budget_data.csv')

profit_losses = []

line_num = 0
month_count = 0
net_profit = 0 
month_list = []
month_profit= 0
change = 0 
change_list = []
avg_change = 0

with open(csvpath, 'r') as csvfile:


    print(type(csvfile))
    
    csvreader = csv.reader(csvfile, delimiter=',')

    print(type(csvreader))
    
    header = next(csvreader)
    line_num += 1
  
    print(f"{header} <---- HEADER")
    
    for row in csvreader:
        
        month_count += 1
        month_list.append(str(row[0]))
        net_profit += int(row[1])
        month_profit = int(row[1])
        profit_losses.append(month_profit)
        
        if change != 0:

            month_profit = int(row[1])
            change = month_profit - change
            change_list.append(change)
            change = int(row[1])
            
        elif change == 0:
            change = int(row[1])  

total_change = sum(change_list)
total_change
avg_change = total_change / len(change_list)
avg_change

month_list.pop(0)
month_list

month_change_dict = dict(zip(month_list, change_list))
month_change_dict  

max_value = max(month_change_dict.values())  
max_keys = [k for k, v in month_change_dict.items() if v == max_value] 

print(max_value, max_keys)

min_value = min(month_change_dict.values())  
min_keys = [k for k, v in month_change_dict.items() if v == min_value] 

print(min_value, min_keys)


print( f'Total Months: {month_count}')
print(f'Total: ${net_profit}')
print(f'Average  Change: ${avg_change}')
print(f'Greatest Increase in Profits: {max_keys} ${max_value}')
print(f'Greatest Decrease in Profits: {min_keys} ${min_value}')


Analysis = Path('analysis.txt')
with open(analysis, 'w') as txtfile:
        txtfile.write(f'\nTotal Months: {month_count}')
        txtfile.write(f'\nTotal: ${net_profit}')
        txtfile.write(f'\nAverage  Change: ${avg_change}')
        txtfile.write(f'\nGreatest Increase in Profits: {max_keys} ${max_value}')
        txtfile.write(f'\nGreatest Decrease in Profits: {min_keys} ${min_value}')