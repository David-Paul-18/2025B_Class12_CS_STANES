#Program 11 - UPDATING BINARY FILE

import pickle
marklist=[]
num=int(input("How many records you want to enter: "))
for loop in range(num):
    rno=int(input(f"Enter the Roll Number of the Student {loop+1}: "))
    name=input(f"Enter the Name of the Student {loop+1}: ")
    mark=float(input(f"Enter the Mark of the Student {loop+1}: "))
    det=[rno,name,mark]
    marklist.append(det)
with open("Mark_List.dat","wb+") as bfile:
    pickle.dump(marklist,bfile)
    bfile.seek(0)
    mlst=pickle.load(bfile)
    print("Old Mark List:",mlst,sep="\n")
    srh=int(input("\nEnter the Roll Number of the Student whose mark is to be updated: "))
    for rec in mlst:
        if rec[0]==srh:
            new=float(input(f"Enter the New Mark of the Student: "))
            rec[2]=new
            bfile.seek(0)
            pickle.dump(mlst,bfile)
            bfile.seek(0)
            updlst=pickle.load(bfile)
            print("Mark List Updated...")
            print(updlst)
            break
    else:
        print("Record Not Found...")
