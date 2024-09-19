#Program 16 - BINARY SEARCH

def BinarySearch(lst,key):
    beg=0
    last=len(ls)-1
    while beg<=last:
        mid=(beg+last)//2
        if search==ls[mid]:
            return mid
        elif search>ls[mid]:
            beg=mid+1
        elif search<ls[mid]:
            last=mid-1
    else:
        return -1
    
ls=eval(input("Enter the elements for the list: "))
opt='Y'
if type(ls)==tuple:
    print("\t!!! ENTER THE ELEMENTS IN SQUARE BRACKETS[] !!!")
else:
    while opt=='Y' or opt=='y':
        ls.sort()
        print("The Sorted List: ", ls)
        search=int(input("\nEnter the element to be searched: "))
        ind=BinarySearch(ls,search)
        if ind==-1:
            print("\n\tSorry! Element is not in the List")
        else:
            print(f"\n\tThe Element {search} is found at Index Position {ind}")
        opt=input("\nDo you want to search any other elements? (Y/N): ")
