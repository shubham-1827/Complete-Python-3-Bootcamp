# lets look at all the methods related to lists in python
lst = [1, 2, 3, 4, 5]
lst.append(6)  # add 6 to the end of the file
print(lst)

lst1 = lst.copy()  # this copies the list to another list
print(lst1)

lst.count(3)  # this counts how many times 3 occured in the lst

help(lst.extend)
lst2 = [7, 8, 9]
lst.extend(lst2)  # it add the lst2 at the end of lst
print(lst)

last_popped = lst.pop()  # this removes the element fro mthe list
# bydefault set to the last element
print(last_popped)

second_popped = lst.pop(1)
print(second_popped)
print(lst)
