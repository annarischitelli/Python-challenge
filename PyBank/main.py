import os
import csv

# Set path for file
budget_data = os.path.join("PyBank", "Resources", "budget_data.csv")

# Set variable value
total_months = 0
total_pl = 0
value = 0
change = 0
dates = []
profits = []

# Read csv file and add to script
with open (budget_data) as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ",")

        # Header row
        csv_header = next(csvreader)
        
        # Read first row
        first_row = next(csvreader)
        total_months += 1
        total_pl += int(first_row[1])
        value = int(first_row[1])

    # Loop through all rows of data starting AFTER first row
        for row in csvreader:
            # Track dates
            dates.append(row[0])
            # Keep track of changes and calculate
            change = int(row[1])-value
            profits.append(change)
            value = int(row[1])
            total_months += 1
            total_pl = total_pl + int(row[1])

        # Create functions for "greatest"
        greatest_increase = max(profits)
        greatest_index = profits.index(greatest_increase)
        greatest_date = dates[greatest_index]
        
        # Create functions for "worst"
        greatest_decrease = min(profits)
        worst_index = profits.index(greatest_decrease)
        worst_date = dates[worst_index]
        avg_change = sum(profits)/len(profits)

# Show all information
print("Financial Analysis")
print("------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_pl)}")
print(f"Avg Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profit: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Loss of Profit: {worst_date} (${str(greatest_decrease)})")