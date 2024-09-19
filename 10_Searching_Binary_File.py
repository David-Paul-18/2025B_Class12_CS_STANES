#Program 10 - SEARCHING IN A BINARY FILE

import pickle
students=[]
num=int(input("How many records you want to enter: "))
for loop in range(num):
    rno=int(input(f"Enter the Roll Number of the Student {loop+1}: "))
    name=input(f"Enter the Name of the Student {loop+1}: ")
    cls=int(input(f"Enter the Class of the Student {loop+1}: "))
    rec=[rno,name,cls]
    students.append(rec)
with open("Students_Data.dat","wb+") as f:
    pickle.dump(students,f)
    f.seek(0)
    ls=pickle.load(f)
    search=int(input("\nEnter the Roll Number of the Student you want to search: "))
    for row in ls:
        if row[0]==search:
            print("\nRecord found...", row,sep="\n")
            break
    else:
        print("\nRecord Not Found")
