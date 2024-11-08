#Program 20 - GENERATING ALTER QUERY - PYTHON SQL INTERFACE

import mysql.connector as sql
conn=sql.connect(host="localhost", user="root", password="mysql123", database="Class12")
if conn.is_connected():
    print("Connection Established Successfully... Process Started...")
crsr=conn.cursor()
print("\n\tAlter Operations for the Table Student")
print("\n1.Add New Column")
print("2.Modify Existing Column")
print("3.Rename Column")
print("4.Exit")
ch=int(input("Select The Operation You Want To Perform: "))
if ch==1:
    newcol=input("\nEnter the New Column Name: ")
    newdat=input(f"Enter the DataType with Size(if any) for {newcol}: ")
    crsr.execute(f"ALTER TABLE Student ADD {newcol} {newdat}")
    conn.commit()
    print("\n\tAdded a New Column Successfully...")
elif ch==2:
    col=input("\nEnter the Column Name to be Modified: ")
    chdat=input(f"Enter the New DataType with New Size(if any) for {col}: ")
    crsr.execute(f"ALTER TABLE Student MODIFY {col} {chdat}")
    conn.commit()
    print(f"\n\tModified {col} Successfully...")
elif ch==3:
    oldname=input("\nEnter the Column Name to be Renamed: ")
    newname=input(f"Enter the New Column Name with New Size(if any) for {oldname}: ")
    crsr.execute(f"ALTER TABLE Student CHANGE {oldname} {newname}")
    conn.commit()
    print(f"\n\tRenamed {oldname} Successfully...")
elif ch==4:
    pass
else:
    print("!!! CHOOSE A VALID OPERATION !!!")
conn.close()
