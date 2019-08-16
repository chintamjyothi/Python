'''Task 
Given an integer, , perform the following conditional actions:
If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird
1<=N<=100'''

N = int(input())

if N < 0 or N > 100:
    print("Enter the number between 0 to 100")

if (N % 2 != 0) or (N % 2 == 0 and N >= 6 and N <= 20):
    print("Weird")
else:
    print("Not Weird")
