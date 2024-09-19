#Program 15 - LINEAR SEARCH

def LinearSearch(lst,key):
    found=None
    for loop in range(len(lst)):
        if lst[loop]==key:
            found=lst.index(lst[loop])
    if found==None:
        return -1
    else:
        return found

ls=eval(input("Enter the elements for the list: "))
opt='Y'
if type(ls)==tuple:
    print("\t!!! ENTER THE ELEMENTS IN SQUARE BRACKETS[] !!!")
else:
    while opt=='Y' or opt=='y':
        search=int(input("\nEnter the element to be searched: "))
        ind=LinearSearch(ls,search)
        if ind==-1:
            print("\n\tSorry! Element is not in the List")
        else:
            print(f"\n\tThe Element {search} is found at Index Position {ind}")
        opt=input("\nDo you want to search any other elements? (Y/N): ")
