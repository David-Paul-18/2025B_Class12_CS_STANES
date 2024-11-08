#Program 18 - GENERATING UPDATE, DELETE QUERIES - PYTHON MYSQL INTERFACE

import mysql.connector as sql
conn=sql.connect(host="localhost", user="root", password="mysql123", database="Class12")
if conn.is_connected():
    print("Connection Established Successfully... Process Started...\n")
crsr=conn.cursor()
print("\tUPDATE STUDENT PHONE NUMBER...")
ch=input("\nDo You Want To Update Any Record?(Y/N): ")
while ch=='Y' or ch=='y':
    name=input("\nEnter the Name of the Student: ")
    phone=int(input(f"Enter the New Phone Number of {name}: "))
    crsr.execute(f"UPDATE Student SET PhoneNo={phone} WHERE Name='{name}'")
    conn.commit()
    print(f"\n\t{name} Phone Number is Updated to {phone} Successfully...")
    ch=input("\nDo You Want To Update Any Other Record?(Y/N): ")

print("\n\tDELETE STUDENT RECORD...")
ch1=input("\nDo You Want To Delete Any Record?(Y/N): ")
while ch1=='Y' or ch1=='y':
    rno=input("\nEnter the Roll Number of the Student: ")
    crsr.execute(f"DELETE FROM Student WHERE RollNo='{rno}'")
    conn.commit()
    print(f"\n\t{rno} Record is Deleted Successfully...")
    ch1=input("\nDo You Want To Delete Any Other Record?(Y/N): ")
conn.close()
