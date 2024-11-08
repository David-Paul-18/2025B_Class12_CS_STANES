#Program 17 - GENERATING CREATE, INSERT QUERIES - PYTHON MYSQL INTERFACE

import mysql.connector as sql
conn=sql.connect(host="localhost", user="root", password="mysql123", database="Class12")
if conn.is_connected():
    print("Connection Established Successfully... Process Started...")
crsr=conn.cursor()
create='''CREATE TABLE Student
(RollNo VARCHAR(20), Name CHAR(20), DOB DATE, PhoneNo BIGINT, Location VARCHAR(30))'''
crsr.execute(create)
conn.commit()
print("Student Table is Created Successfully...")
print("\tEnter Data for the Table Student:")
rec=int(input("How many records do you want to insert in the Table Student? "))
print()
for loop in range(rec):
    rno=input(f"Enter the Roll Number of the Student {loop+1}: ")
    name=input(f"Enter the Name of the Student {loop+1}: ")
    dob=int(input(f"Enter the DOB of the Student {loop+1} in YYYYMMDD format: "))
    phone=int(input(f"Enter the Phone Number of the Student {loop+1}: "))
    loc=input(f"Enter the Location of the Student {loop+1}: ")
    crsr.execute(f"INSERT INTO Student VALUES('{rno}','{name}',{dob},{phone},'{loc}')")
    conn.commit()
    print(f"\t{loop+1} Records Inserted Successfully...\n")
conn.close()
