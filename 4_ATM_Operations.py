#Program 4 - ATM OPERATIONS

Balance=120000
ch='Y'
AcNo=int(input("Enter your Account Number: "))
Name=input("Enter your Name: ")
def Dep():
    global Balance
    print("\t\t\tDEPOSIT")
    print("\t\t\t-------")
    print("Your Existing Balance is: ",Balance)
    depamt=int(input("Enter the amount to be deposited: "))
    Balance+=depamt
    print(f"\n\t\t\tAmount of Rs.{depamt} is Credited Successfully")
    return Balance
def With():
    global Balance
    print("\t\t\tWITHDRAWAL")
    print("\t\t\t----------")
    print("Your Existing Balance is: ",Balance)
    withamt=int(input("Enter the amount to be withdrawn: "))
    Balance-=withamt
    print(f"\n\t\t\tAmount of Rs.{withamt} is Debited Successfully")
    return Balance
def BalEnq():
    print("\n\t\tYour Account Number: ",AcNo)
    print("\t\tYour Name: ",Name)
    print("\n\t\t\tYour Account Balance is: ",Balance)
while ch=='Y' or ch=='y':
    print("\n\t\t\tWELCOME",Name)
    print("\n\t1.Deposit")
    print("\t2.Withdrawal")
    print("\t3.Balance Enquiry")
    print("\t4.Exit\n")
    choice=int(input("Choose your transaction: "))
    if choice<1 or choice>4:
        print("\n!!! CHOOSE A VALID TRANSACTION !!!\n")
    elif choice==1:
        print("\nAccount Number: ", AcNo)
        print("Name: ", Name)
        print("\n\tYour Account Balance is: ",Dep())
    elif choice==2:
        print("\nAccount Number: ", AcNo)
        print("Name: ", Name)
        print("\n\tYour Account Balance is: ",With())
    elif choice==3:
        BalEnq()
    elif choice==4:
        break
    ch=input("\nDo you want to continue transaction(Y/N)? ")
    
