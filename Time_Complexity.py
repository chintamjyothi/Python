'''
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
 
'''
# Time Complexity

h = int(input("Enter the height: "))
h = h+1

for i in range(h,1,-1): #(n) -> Time
	print(' ' * (i-2), '* ' * (h- i+1))
