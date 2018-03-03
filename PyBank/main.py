import os
import csv

TotalMon = 0
TotalRev = 0
init_Rev = 943690
RevChange = 0
AveRev_Change = 0
TotalRev_Change = 0
MaxIncRev = 0
MaxIncMonth = ""
MaxDecRev = 0
MaxDecRevMonth = ""

csvpath = os.path.join("budget_data_2.csv")
with open(csvpath, 'r', encoding='utf-8') as csvfile:
    csvread = csv.reader(csvfile)

    next(csvread, None)

    for row in csvread:
        TotalMon = TotalMon + 1
        TotalRev = TotalRev + int(row[1])
        RevChange = int(row[1])-init_Rev
        TotalRev_Change = TotalRev_Change + RevChange
        if(RevChange > MaxIncRev):
            MaxIncRev = RevChange
            MaxIncMonth = row[0]
        elif(RevChange < MaxDecRev):
            MaxDecRev = RevChange
            MaxDecMonth = row[0]
            init_Rev = int(row[1])

AveRev_Change = TotalRev_Change/(TotalMon - 1)


print("Financial Analysis")
print("----------------------")
print("Total Months: " + str(TotalMon))
print("Total Revenue: $" + str(TotalRev))
print("Average Revenue Change: $" + str(AveRev_Change))
print("Greatest Increase in Revenue: " + MaxIncMonth + " $" + str(MaxIncRev))
print("Greatest Decrease in Revenue: " + MaxDecMonth + " $" + str(MaxDecRev))

with open("C:\Documents\Revenue.txt", 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------\n")
    txtfile.write("Total Months: " + str(TotalMon)+"\n")
    txtfile.write("Total Revenue: $" + str(TotalRev)+"\n")
    txtfile.write("Average Revenue Change: $" + str(AveRev_Change)+"\n")
    txtfile.write("Greatest Increase in Revenue: " + MaxIncMonth + " $" + str(MaxIncRev)+"\n")
    txtfile.write("Greatest Decrease in Revenue: " + MaxDecMonth + " $" + str(MaxDecRev)+"\n")
