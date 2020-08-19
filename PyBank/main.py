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
    totals = []

    #Append csv data into contents by row
    for row in csvreader:
        contents.append(row)
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

# create difference list to capture differcences in the totals list
difference = []
for i in range(len(totals)-1):
    difference.append(totals[i+1]-totals[i])
    #Note: List comprehension version: # differences = ([totals[i+1]-totals[i] for i in range(len(totals)-1)])

# Average = sum of difference / length of difference
averagechange = round(sum(difference)/len(difference),2)

# Output to terminal
print("Financial Analysis")
print("-"*30)
print(f"Total Months: {count_csvrecords}")
print(f"Total: ${profitloss}")
print(f"Average Change: ${averagechange}")
print(f"Greatest Increase in Profits: {greatestincreasemonth} (${greatestincrease})")
print(f"Greatest Decrease in Profits: {greatestdecreasemonth} (${greatestdecrease})")

# Write results to text file

output_path = os.path.join("analysis","output.txt")

with open(output_path,"w") as text:
    text.write("Financial Analysis\n")
    text.write("-"*30)
    text.write("\n")
    text.write(f"Total Months: {count_csvrecords}\n")
    text.write(f"Total: ${profitloss}\n")
    text.write(f"Average Change: ${averagechange}\n")
    text.write(f"Greatest Increase in Profits: {greatestincreasemonth} (${greatestincrease})\n")
    text.write(f"Greatest Decrease in Profits: {greatestdecreasemonth} (${greatestdecrease})\n")
text.close()