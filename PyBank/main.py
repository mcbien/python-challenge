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
    

# print(contents)
# print(totals)


# Determine the number of items in contents
count_csvrecords = len(contents)

# Determine the Profit / Loss column total
profitloss = 0
for i in totals:
     profitloss = profitloss + i

    
# Output to terminal
print("Financial Analysis")
print("-"*30)
print(f"Total Months: {count_csvrecords}")
print(f"Total: {profitloss}")