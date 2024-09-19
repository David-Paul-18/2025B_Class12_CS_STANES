#Program 2 - SUM, PRODUCT, SQUARES OF ELEMENTS OF LIST

Sum=0
Product=1
fact=1
sqlst=[]
elems=int(input("Enter the number of elements for the List: "))
List=[]

for loop in range(elems):
    data=int(input(f"Enter element {loop+1}: "))
    List.append(data)
print("Your List -->",List)

for e in List:
    Sum=Sum+e
    Product=Product*e
    Square=e*e
    sqlst.append(Square)
print("The Sum of the Elements of your List is: ",Sum)
print("The Product of the Elements of your List is: ",Product)
print("The Squares of the Elements of your List is: ",sqlst)
