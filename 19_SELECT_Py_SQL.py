#Program 19 - GENERATING SELECT QUERY - PYTHON MYSQL INTERFACE

import mysql.connector as sql
conn=sql.connect(host="localhost", user="root", password="mysql123", database="Class12")
if conn.is_connected():
    print("Connection Established Successfully... Process Started...\n")
crsr=conn.cursor()
select="SELECT * FROM Student ORDER BY DOB"
crsr.execute(select)
table=crsr.fetchall()
count=crsr.rowcount
print(f"The Number of Records retrieved are: {count}")
print("The Records in the Table Student:")
for row in table:
    print(row)

ch=input("\nDo You Want To Retrieve Any Specific Number Of Records?(Y/N): ")
while ch=='Y' or ch=='y':
    rec=int(input("\nHow many Records do you need? "))
    crsr.execute(select)
    data=crsr.fetchmany(rec)
    count2=crsr.rowcount
    print(f"\nThe Number of Records now retrieved are: {count2}")
    print(f"{rec} Records from the Table Student:")
    for record in data:
        print(record)
    ch=False
conn.close()
