# range() function is the generator used to generate the list of numbers with the minimum overhead
list1 = list(range(10))
print(list1)

# the range() function takes three parameters (start, stop, step-size)
list2 = list(range(0, 100, 4))
# now there will be jumps of 4
print(list2)

# enumerate Function
# what this does is it create the list of tuple pairs of (idx, element)
list3 = list(enumerate(list2))
print(list3)

for i, ele in list3:
    print(f"the {i} element is {ele}")

# zip function -> this is also a generator
# it is also like enumerate function, but it just do the same tuple packing with two lists
# the list which is smaller will be preffered
list1 = list(range(0, 20, 3))
list2 = list(range(12, 54, 2))
print(len(list1))
print(len(list2))

# if we now zip above 2 then the final length of zip will be of size of list1 which is 7
zipped_list = list(zip(list1, list2))
print(zipped_list)
print(len(zipped_list))

# the in operator
# it checks if something is present 'in' list, tuple, set, string, dict, etc ...
list1 = [1, 2, 3, 4, 5, 6]
print(6 in list1)  # this will return true
print(10 in list1)  # this will return false

# the in operator also looks for the substrings as well
s = "shubham tiwari"
print("tiwari" in s)  # true
print("shubh" in s)  # true

# similar case : we have 'not in' operator
print("manish" not in s)

# the min and max functions
list1 = list(range(0, 100, 3))
from random import shuffle

shuffle(list1)

minimum_value = min(list1)
max_value = max(list1)
print(minimum_value, max_value)

# wrte a program to select 5 random elements from list 1
from random import randint

for value in range(5):
    print(list1[randint(0, len(list1) - 1)], end=" ")
