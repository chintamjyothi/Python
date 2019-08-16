#Input List

n = int(input("Enter the size of List : "))

input_list =  list()

print(input_list)

print("Enter the number in the List")

for i in range(0,n):
    num = int(input())
    input_list.append(num)

print("The List is : " + str(input_list))

# pop
# Syntex : list.pop(index)

input_list.pop(n-1)

print("The List after Pop is : " + str(input_list))

# Lenght of List

print("The Length of List is : " + str(len(input_list)))

# Changing List index value

input_list[0] = int(input("Enter the new value for first index : "))

print("The new List is after changing first index value : " + str(input_list))


# Slicing

# Syntax : slicing = input_list[start:stop:step]

print("List after Slicing")

print(input_list[0:len(input_list):2])

print(input_list[0::]) # Print all element in list

# Reverse

print("Reverse List")

print(input_list[-1:-(len(input_list)+1):-1])

print(input_list[::-1])

print(list(reversed(input_list)))

# max, min and avg number in list

print("Max number present in List")

print(max(input_list))

print("Min number present in List")

print(min(input_list))

print("Average of all numbers in List")

total = 0

for i in range(0,len(input_list)):
    total = total + input_list[i]

print(total/len(input_list))

print("Sum of all numbers in List : " + str(total))

# sorting of list

print("The List after shorting")

print(sorted(input_list))

# Logical code for reversing the List

for i in range(0,(len(input_list)-1)):
    for j in range(i+1,len(input_list)):
        if(input_list[i] > input_list[j]):
            temp = input_list[i]
            input_list[i] = input_list[j]
            input_list[j] = temp


print(input_list)
