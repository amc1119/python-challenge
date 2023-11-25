# Allow file paths to be created across operating systems
import os
import string

# Module for reading CSV files
import csv

budget_csv = os.path.join('Resources', 'budget_data.csv')
analysis_path = "Analysis/final_analysis.txt"

with open(budget_csv, 'r') as budget_file:

    net_total = 0
    total_months = 0 
    previous_profit = 0
    change = 0
    total_change = 0
    change_counter = 0
    greatest_increase = ["", 0]
    greatest_decrease = ["", 0]

    # CSV reader specifies delimiter and "data" holds the contents
    budget_csvreader = csv.reader(budget_file, delimiter=',')

    # Read the header row first
    data_header = next(budget_csvreader)

    # Read each row of data after the header
    for row in budget_csvreader:
        total_months = total_months + 1
        net_total = net_total + int(row[1])
        current_profit = int(row[1])

        if previous_profit != 0:
            change = current_profit - previous_profit
            total_change = total_change + change
            change_counter += 1

        previous_profit = current_profit 

        if change > greatest_increase[1]:
            greatest_increase[1] = change
            greatest_increase[0] = row[0]

        if change < greatest_decrease[1]:
            greatest_decrease[1] = change
            greatest_decrease[0] = row[0]

output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${round(total_change/change_counter, 2)}
Greatest Increase in Profits: {greatest_increase[0]} $({greatest_increase[1]})
Greatest Decrease in Profits: {greatest_decrease[0]} $({greatest_decrease[1]})
"""

print(output)

with open(analysis_path, "w") as output_file:
    output_file.write(output)
