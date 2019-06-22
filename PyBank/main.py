##### main.py
import csv
import os
import sys

os.chdir("C:\\Users\\gutie\\Dropbox\\Documentos Insumos\\PREWORK_CGF\\Module-3\\Homework\\PyBank\\")
print(os.getcwd())
sys.stdout = open('output.txt', 'w')

i=0
Total = 0
t0=0
t1=0
avChange=0
gIP=0
gDP=0
fIP=""
fDP=""

with open('budget_data.csv','r', newline='') as file:
    budget=csv.reader(file, delimiter=',')
    print(budget)
    headers=next(budget)
    print(f"CSV Header: {headers}")
    for row in budget:
            i=i+1
            Total=Total+int(row[1])
            t1=int(row[1])
            Change=(t1-t0)
            avChange=avChange+Change
            t0=int(row[1])
            if(i==1):
                avChange=0
            if(Change>gIP):
                gIP=Change
                fIP=row[0]
            if(Change<gDP):
                gDP=Change
                fDP=row[0]
    
    print("\n Financial Analysis \n -----------------------------\n")
    print(f"Total Months: {i}")
    print(f"Total: ${Total}")
    print(f"Average  Change: ${avChange/(i-1)}")
    print(f"Greatest Increase in Profits: {fIP}(${gIP})")
    print(f"Greatest Decrease in Profits: {fDP}(${gDP})")
    
    sys.stdout.close()