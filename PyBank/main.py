# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'budget_data.csv')

#  initializing variables and list
row_count_budget_data = 0
net_total_amount = 0
average_change = 0

greatest_increase_in_profits = 0
greatest_decrease_in_profits = 0

index_greatest_increase = 0
index_greatest_decrease = 0

first_list_budget_data = []
difference_budget_data = []
list_mmm_yyyy = []

#  reading the file and storing it in a list while storing total months and
#  total amount in a variable and date (mmm-yyyy) in a list
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row without any other operation
    next (csvreader,None)

    for row in csvreader:

        row_count_budget_data = row_count_budget_data + 1
        net_total_amount = int(net_total_amount) + int(row[1])
        list_mmm_yyyy.append(row[0])
        first_list_budget_data.append(float(row[1]))

#  calculating the difference of rows to calculate the average of changes
for i in range(len(first_list_budget_data)-1):
    difference_budget_data.append(float(first_list_budget_data[i+1])-float(first_list_budget_data[i]))

#  calculating average and greates increase and greatest decrease in next 3 lines
average_change = round(sum(difference_budget_data)/len(difference_budget_data),2)
greatest_increase_in_profits = max(difference_budget_data)
greatest_decrease_in_profits = min(difference_budget_data)

#  calculating the index of the greatest increase and greatest decrease to determine
#  the month and year from the mmm_yyyy list
for i in range(len(difference_budget_data)):
    if (difference_budget_data[i] == greatest_increase_in_profits ):
        index_greatest_increase = i+1
    if (difference_budget_data[i] == greatest_decrease_in_profits ):
        index_greatest_decrease = i+1

#  printing to terminal
print("")
print ("     Financial Analysis    ")
print("------------------------------")
print (f"Total Months: {row_count_budget_data}")
print (f"Total: {'${}'.format(net_total_amount)}")
print (f"Average Change: {'${}'.format(average_change)}")
print("Greatest Increase in Profits: " + str(list_mmm_yyyy[index_greatest_increase]) + " (" +  str('${}'.format(int(difference_budget_data[index_greatest_increase-1])) ) +")")
print("Greatest Decrease in Profits: " + str(list_mmm_yyyy[index_greatest_decrease]) + " (" +  str('${}'.format(int(difference_budget_data[index_greatest_decrease-1])) ) +")")

#  Set variable for output file
output_file = os.path.join("output_budget_data.csv")

#  printing to output file
#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["     Financial Analysis    "])
    writer.writerow(["------------------------------"])
    writer.writerow([f"Total Months: {row_count_budget_data}"])
    writer.writerow([f"Average Change: {'${}'.format(average_change)}"])
    writer.writerow(["Greatest Increase in Profits: " + str(list_mmm_yyyy[index_greatest_increase]) + " (" +  str('${}'.format(int(difference_budget_data[index_greatest_increase-1])) ) +")"])
    writer.writerow(["Greatest Decrease in Profits: " + str(list_mmm_yyyy[index_greatest_decrease]) + " (" +  str('${}'.format(int(difference_budget_data[index_greatest_decrease-1])))+")"])
