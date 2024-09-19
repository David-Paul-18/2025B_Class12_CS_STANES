#Program 5 - AREA OF SHAPES

print("\t\t\tAREA OF SHAPES")
print("\t\t\t--------------")
print("1.Area of Square")
print("2.Area of Rectangle")
print("3.Area of Triangle")
print("4.Area of Circle")
print("5.Exit")
choice=int(input("Enter your choice: "))
import math
def square(side):
    sqr=side*side
    print("The Area of Square: ",sqr)
def rectangle(length,breadth):
    rect=length*breadth
    print("The Area of Rectangle: ",rect)
def triangle(base,height):
    tri=0.5*base*height
    print("The Area of Triangle: ",tri)
def circle(radius):
    circ=math.pi*radius**2
    print("The Area of Circle: ",circ)

if choice==1:
    s=eval(input("Enter the value of Side: "))
    square(s)
elif choice==2:
    l=eval(input("Enter the value of Length: "))
    b=eval(input("Enter the value of Breadth: "))
    rectangle(l,b)
elif choice==3:
    bse=eval(input("Enter the value of Base: "))
    h=eval(input("Enter the value of Height: "))
    triangle(bse,h)
elif choice==4:
    r=eval(input("Enter the value of Radius: "))
    circle(r)
elif choice==5:
    pass
else:
    print("INVALID SELECTION!!!")

