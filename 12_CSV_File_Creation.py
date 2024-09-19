#Program 12- CREATING CSV FILE

import csv
invntry={}
stkno=[]
stkname=[]
qty=[]
choice='Y'
print("\t\t\tINVENTORY")
print("\t\t\t*********")
while choice=='Y' or choice=='y':
    sno=input("Enter the Stock Serial Number: ")
    name=input("Enter the Stock Name: ")
    q=input("Enter the Quantity: ")
    stkno.append(sno)
    stkname.append(name)
    qty.append(q)
    choice=input("Do you want to continue?(Y/N): ")
invntry.update(StockNo=stkno,StockName=stkname,Quantity=qty)

with open("Inventory.csv","w+", newline="\n") as cfile:
    w=csv.writer(cfile)
    w.writerow(invntry.keys())
    for loop in range(len(stkno)):
        w.writerow([invntry['StockNo'][loop],invntry['StockName'][loop],invntry['Quantity'][loop]])
    r=csv.reader(cfile)
    cfile.seek(0)
    for row in r:
        print(row)
