'''
List-->
=======
Description: Lists are ordered, mutable 
(changeable) collections that allow duplicate elements. 
They are defined by square brackets [].
'''

fruits = ["apple", "banana", "cherry"]
print(fruits[1])           # Access item
fruits.append("orange")    # Add item

my_list = [1, 2, 3, 4, 5]

'''
Operations:
    Access elements: my_list[0] (returns 1)
    Modify elements: my_list[1] = 10 (changes second element to 10)
    Append elements: my_list.append(6)
    Remove elements: my_list.remove(3)
'''

print(my_list)  # print the all list
print(my_list[1]) # print the contained value of the index 1
my_list[2] = 7  # index 2  = value 3 will change the 7
print(my_list)
