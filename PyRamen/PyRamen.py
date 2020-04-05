from pathlib import Path
import csv

menu_data_csv = Path('menu_data.csv')
sales_data_csv = Path('sales_data.csv')

menu = []
sales = []
line_num = 0

with open (menu_data_csv, "r") as csvfile:
    print(type(menu_data_csv))
    
    csv_reader = csv.reader(csvfile, delimiter=',')
   
    print(type(csv_reader))
    header = next(csv_reader)
    print(f"{header} <---- HEADER")
    for row in csv_reader:
        menu.append(row)
        print(menu)
        
with open (sales_data_csv, 'r') as csvfile:
    print(type(sales_data_csv))
    
    csv_reader = csv.reader(csvfile, delimiter=',')
    print(type(csv_reader))
    header = next(csv_reader)
    print(f"{header} <---- HEADER")
    for row in csv_reader:
        sales.append(row)

report = {}

    for sales_row in sales:
    
    sales_menu_item = sales_row[4] 
    quantity = sales_row[3]
    
    if sales_menu_item not in report:
        report[sales_menu_item] = {"01-count": 0, "02-revenue": 0, "03-cogs": 0, "04-profit": 0}
    else:
        continue
        
    for menu_row in menu:
    
        menu_item = menu_row[0]
        menu_price = menu_row[3]
        menu_cost = menu_row[4]
    
        if sales_menu_item == menu_item:
            report[sales_menu_item]["01-count"] += int(quantity)
            report[sales_menu_item]["02-revenue"] += (int(menu_price) * int(quantity))
            report[sales_menu_item]["03-cogs"] += (int(menu_cost) * int(quantity))
            report[sales_menu_item]["04-profit"] += profit * int(quantity)
        elif sales_menu_item != menu_item:
            continue

        for item, valuesdict in report.items():
    
            for key in valuesdict:
                count = report[sales_menu_item]["01-count"]
                cogs = report[sales_menu_item]["03-cogs"]
                revenue = report[sales_menu_item]["02-revenue"]
        
            if key == "04-profit":
            report[sales_menu_item][key] = revenue - cogs
            else:
                continue