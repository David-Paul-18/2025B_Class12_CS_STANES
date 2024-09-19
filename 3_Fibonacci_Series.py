#Program 3 - FIBONACCI SERIES

def fibonacci(n):
    a=0
    b=1
    if n<=0:
        print("Invalid Input !!!")
    elif n==1:
        print("Fibonacci Series:\n",a)
    else:
        print("Fibonacci Series:\n",a,b,end=" ")
        for loop in range(n-2):
            c=a+b
            print(c,end=" ")
            a=b
            b=c
num=int(input("Enter the number of Fibonacci Series to be generated: "))
fibonacci(num)
