'''Task 
Read two integers from STDIN and print three lines where:
The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.'''

    a = int(input())
    b = int(input())

    print("The sum of a and b is")
    print(a+b)

    print("The difference of a and b is")
    if a > b:
        print(a-b)
    else:
        print(b-a)

    print("The product of a and b is")
    print(a*b)
