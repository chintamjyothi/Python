''' Program for printing Pyramid
          *           
        * * *         
      * * * * *       
    * * * * * * *     
  * * * * * * * * *   
* * * * * * * * * * *
'''

print("Enter the size of X-axis")
x = int(input())

for i in range(0,x):
    for j in range(0,i+1):
        if j <= i:
            print("* ",end="")
        else:
            print("  ",end="")
    print()
    

print()

for i in range(1,x+1):
    for j in range(1,x+1):
        if i+j >= x+1:
            print("* ",end="")
        else:
            print("  ",end="")
    print()

print()

for i in range(0,x):
    for j in range(-(x+1),x):
        if j <= i and j >= -i:
            print("* ",end="")
        else:
            print("  ",end="")
    print()


print()

for i in range(1,x+1):
    for j in range(1,2*x):
        if j >= x+1-i and j <= x-1+i:
            print("* ",end="")
        else:
            print("  ",end="")
    print()
