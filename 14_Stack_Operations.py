#Program 14 - STACK OPERATIONS

def Push(stk, elem):
    stk.append(elem)
    top=len(stk)-1

def Pop(stk):
    if stk==[]:
        return 'Underflow'
    else:
        del_elem=stk.pop()
        if len(stk)==0:
            top=None
        else:
            top=len(stk)-1
        return del_elem

def Peek(stk):
    if stk==[]:
        return 'Underflow'
    else:
        top=len(stk)-1
        return stk[top]

def Display(stk):
    if stk==[]:
        print("\n\tStack is Empty !")
    else:
        top=len(stk)-1
        print("\nStack contains:")
        print("\t",stk[top],"<- Top element")
        for loop in range(top-1, -1, -1):
            print("\t",stk[loop])

Stack=[]
top=None
while True:
    print("\n\t\t\tSTACK OPERATIONS")
    print("\t\t\t****************")
    print("1.Push")
    print("2.Pop")
    print("3.Peek")
    print("4.Display")
    print("5.Exit")
    ch=int(input("Enter your choice: "))
    if ch<1 or ch>5:
        print("\n!!! INVALID SELECTION !!! Choose from 1 to 5")
    elif ch==1:
        Element=int(input("Enter the element: "))
        Push(Stack, Element)
    elif ch==2:
        d_elem=Pop(Stack)
        if d_elem=='Underflow':
            print("\n\tUnderflow ! The Stack is Empty")
        else:
            print("\n\tThe Popped element is: ", d_elem)
    elif ch==3:
        top_elem=Peek(Stack)
        if top_elem=='Underflow':
            print("\n\tUnderflow ! The Stack is Empty")
        else:
            print("\n\tThe Topmost element is: ", top_elem)
    elif ch==4:
        Display(Stack)
    elif ch==5:
        break



    
