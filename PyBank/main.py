import csv 
file_load = ("Resources/budget_data.csv")
file_write = ("analysis/budget_analysis.txt")
monthcount = 0
total_net = 0
change_list = []
month_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999]
with open (file_load, 'r') as budget_data: 
    reader = csv.reader(budget_data)
    headers = next(reader)
    first_row = next(reader)
    monthcount +=1
    total_net += int(first_row[1])
    previous_net = int(first_row[1])
    #print(total_net)
    #monthcount = 0

    for row in reader:
        monthcount = monthcount + 1
        total_net += int(row[1])
        net_change = int(row[1])- previous_net
        previous_net = int(row[1])
        change_list += [net_change] 
        month_list += [row[0]]
        if net_change > greatest_increase [1]:
            greatest_increase[0]= row[0]
            greatest_increase[1]=net_change
        if net_change < greatest_decrease [1]:
            greatest_decrease[0]=row[0]
            greatest_decrease[1]=net_change
net_average = sum(change_list)/len(change_list) 


output = (f"""
Financial Analysis
----------------------------
Total Months: {monthcount}
Total: ${total_net:,}
Average Change: ${net_average:,.2f}
Greatest Increase in Profits:{greatest_increase[0]} (${greatest_increase[1]:,})
Greatest Decrease in Profits:{greatest_decrease[0]} (${greatest_decrease[1]:,})""")
print (output)

with open (file_write, "w") as file:
    file.write(output)




   