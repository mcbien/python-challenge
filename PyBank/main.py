# Import Modules
import os
import csv

# Set relative filepath
filepath = os.path.join("Resources","budget_data.csv")

with open(filepath, "r") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")

    # Segregate header
    header = next(csvreader)

    # Create empty coontents list to hold csv data
    contents = [] # used to capture full contents of csv file
    months = [] # used to pature totals column of csv file
    totals = [] # used to pature totals column of csv file


    #Append csv data into contents by row
    for row in csvreader:
        contents.append(row)
        months.append(row[0])
        totals.append(int(row[1]))

# Determine the number of items in contents
count_csvrecords = len(contents)

#Convert Profit / Loss column in contents to integer
for row in contents:
    row[1] = int(row[1])

# Determine the Profit / Loss column total
profitloss = 0
greatestincrease = 0
greatestdecrease = 0

for row in contents:
    profitloss = profitloss + row[1]
    if row[1] > greatestincrease:
        greatestincrease = row[1]
        greatestincreasemonth = row[0]
    elif row[1] < greatestdecrease:
        greatestdecrease = row[1]
        greatestdecreasemonth = row[0]

# for i in totals:
#     profitloss = profitloss + i
#     if i > greatestincrease:
#         greatestincrease = i
  
#         greatestdecrease = i


# print(greatestincrease)

# print(greatestdecrease)


# Output to terminal
print("Financial Analysis")
print("-"*30)
print(f"Total Months: {count_csvrecords}")
print(f"Total: ${profitloss}")
print(f"Greatest Increase in Profits: {greatestincreasemonth} (${greatestincrease})")
print(f"Greatest Decrease in Profits: {greatestdecreasemonth} (${greatestdecrease})")