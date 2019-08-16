# Fibonacci Series

def fab(n):
    if n == 1:
        print(0)
    elif n == 2:
        print(0)
        print(1)
    else:
        print(0)
        print(1)
        a = [None] * n
        a[0]=0
        a[1]=1
        for i in range(2,n):
            a[i]=a[i-1]+a[i-2]
            print(a[i])

num = int(input("Enter Your Number : "))
fab(num)

def fib(n):
    if n == 1:
        print(0)
    elif n == 2:
        print(0)
        print(1)
    else:
        print(0)
        print(1)
        a = [None] * n
        a[0]=0
        a[1]=1
        for i in range(2,n):
            a[i]=a[i-1]+a[i-2]
            if a[i] <= 100:
                print(a[i])
                


print("Fibonacci Series till 100 : ")
fib(100)
