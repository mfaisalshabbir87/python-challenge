import csv
import os

# choose file 1 or 2
file_num = 1

# create file path and save as file
file = os.path.join('raw_data', 'budget_data_'+ str(file_num) +'.csv')


months = []
revenue = []

#read csv and parse data into lists

with open(file, 'r') as csvfile:
    csvread = csv.reader(csvfile)

    next(csvread, None)

    for row in csvread:
        months.append(row[0])
        revenue.append(int(row[1]))

#find total months
total_months = len(months)

#create largest increase, decrease variables and set them equal to the first revenue record

largest_inc = revenue[0]
largest_dec = revenue[0]
total_revenue = 0

#loop through revenue indices

for r in range(len(revenue)):
    if revenue[r] >= largest_inc:
        largest_inc = revenue[r]
        great_inc_month = months[r]
    elif revenue[r] <= largest_dec:
        largest_dec = revenue[r]
        great_dec_month = months[r]
    total_revenue += revenue[r]

#calculate average_change
average_change = round(total_revenue/total_months, 2)


output_path = os.path.join('Output','pybank_output_' + str(file_num) + '.txt')

# print the summary
with open(output_path, 'w') as writefile:
    writefile.writelines('Financial Analysis\n')
    writefile.writelines('---------' + '\n')
    writefile.writelines('Total Revenue: $' + str(total_revenue) + '\n')
    writefile.writelines('Total Months: ' + str(total_months) + '\n')
    writefile.writelines('Average Revenue Change: $' + str(average_change) + '\n')
    writefile.writelines('largest Increase in Revenue: ' + great_inc_month + ' ($' + str(largest_inc) + ')'+ '\n')
    writefile.writelines('largest Decrease in Revenue: ' + great_dec_month + ' ($' + str(largest_dec) + ')')

#prints to terminal
with open(output_path, 'r') as readfile:
    print(readfile.read())
