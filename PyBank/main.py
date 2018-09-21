import os

buget_data = os.path.join("..", "PyBank", "budget_data.csv")

import datetime

import csv

budget_data = []

profit_loss = []

with open('budget_data.csv', newline="") as csv_file:

    csv_reader = csv.reader(csv_file, delimiter="-")
    
    header = next(reader)

    budget_data = []

    for row in csv_reader:

        row = [date, profit_loss]

        date.append(row[0])

        profit_loss.append(int(row[1]))

print()

print(date)

print(profit_loss)

cleaned_csv = zip(date, profit_loss)

output_file = os.path.join("budge_data_final.csv")

with open(output_file, "w", newline="") as datafile:

    writer = csv.writer(datafile) 


    writerrow(["Date", "Profit_Loss"])

    writer.writerow(cleaned_csv)


          

        
        