# Import Modules
import os
import csv

# Set relative filepath
filepath = os.path.join("Resources","election_data.csv")

with open(filepath, "r") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")

    # Segregate header
    header = next(csvreader)

    # Create empty coontents list to hold csv data
    contents = [] # used to capture full contents of csv file
    candidates = [] # used to capture the list of candidates


    # Append csv data into contents by row
    for row in csvreader:
        contents.append(row)
        candidates.append(row[2])
        
totalvotes = len(contents)

#print(header)
#print(contents[0])

# # Capture unique candidates
uniquecandidates = []
for i in candidates:
    if i not in uniquecandidates:
        uniquecandidates.append(i)

# Tablulate unique votes by candidate:
votescandidate1 = 0
votescandidate2 = 0
votescandidate3 = 0
votescandidate4 = 0

for i in contents:
    if i[2] == uniquecandidates[0]:
        votescandidate1 = votescandidate1 + 1
    elif i[2] == uniquecandidates[1]:
        votescandidate2 = votescandidate2 + 1
    elif i[2] == uniquecandidates[2]:
        votescandidate3 = votescandidate3 + 1
    elif i[2] == uniquecandidates[3]:
        votescandidate4 = votescandidate4 + 1

# Calculate percentages
pervotes1 = round(votescandidate1 / totalvotes * 100,3)
pervotes2 = round(votescandidate2 / totalvotes * 100,3)
pervotes3 = round(votescandidate3 / totalvotes * 100,3)
pervotes4 = round(votescandidate4 / totalvotes * 100,3)

# # Determine winner
if votescandidate1 > votescandidate2 and votescandidate1 > votescandidate3 and votescandidate1 > votescandidate4:
    winner = uniquecandidates[0]
elif votescandidate2 > votescandidate1 and votescandidate2 > votescandidate3 and votescandidate2 > votescandidate4:
    winner = uniquecandidates[1]
elif votescandidate3 > votescandidate1 and votescandidate3 > votescandidate2 and votescandidate3 > votescandidate4:
    winner = uniquecandidates[2]
else:
    winner = uniquecandidates[3]

print("Election Results")
print("-"*30)
print(f"Total Votes: {totalvotes}")
print("-"*30)
print(f"{uniquecandidates[0]}: {pervotes1}% ({votescandidate1}")
print(f"{uniquecandidates[1]}: {pervotes2}% ({votescandidate2}")
print(f"{uniquecandidates[2]}: {pervotes3}% ({votescandidate3}")
print(f"{uniquecandidates[3]}: {pervotes4}% ({votescandidate4})")
print("-"*30)
print(f"Winner: {winner}")
print("-"*30)

output_path = os.path.join("analysis","election results.txt")

with open(output_path,"w") as text:
    text.write("Election Results\n")
    text.write("-"*30)
    text.write(f"\nTotal Votes: {totalvotes}\n")
    text.write("-"*30)
    text.write(f"\n{uniquecandidates[0]}: {pervotes1}% ({votescandidate1})\n")
    text.write(f"{uniquecandidates[1]}: {pervotes2}% ({votescandidate2})\n")
    text.write(f"{uniquecandidates[2]}: {pervotes3}% ({votescandidate3})\n")
    text.write(f"{uniquecandidates[3]}: {pervotes4}% ({votescandidate4})\n")
    text.write("-"*30)
    text.write(f"\nWinner: {winner}\n")
    text.write("-"*30)
text.close()