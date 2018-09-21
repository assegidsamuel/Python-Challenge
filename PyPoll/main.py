import os

election_data = os.path.join("..", "PyPoll", "election_data.csv")

import csv

voterId = []

county = []

candidate = []

with open('election_data', newline="-") as csv_file:
    
    csv_reader = csv.reader(csv_file, delimiter="")
    
    header = next(row)
    
    election_data =[]
    
    for row in csv_reader:
        
       voter_ID.append(row[0])

       county.append(row[1])

       candidate.append(row[2])

print(voter_ID)

print(county)

print(candidate)

cleaned_csv = zip(voter_ID, county, candidate)

output_file = os.path.join("new_election_data.csv")

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile) 

    writerrow(["Voter_ID", "County", "Candidate"])
    writer.writerow(cleaned_csv)