# Prime Number

from math import *

def is_prime(n):
    count = 0 
    if n < 0:
        print("Please enter positive integer")
    elif (n == 0) or (n == 1):
        print("Not a Prime Number")
    else:
        for i in range(2,int(sqrt(n))+1):
            if n % i == 0:
                count = count + 1
        if count > 0:
            print("Not a Prime Number")
        else:
            print("Prime Number")

print("Enter a Number : ")

num = int(input())

is_prime(num)

print()

# Prime Number till 100

print("Prime Numbers till 100")

total = 0

for i in range(2,101):
    cnt = 0
    for j in range(2,int(sqrt(i))+1):
        if i % j == 0:
            cnt = cnt + 1
        else:
            pass
    if cnt == 0:
        print(i)
        total = total + 1

print()
print("Total Numbet of Prime Numbers till 100 : " + str(total))
