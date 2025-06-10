list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in list_1:
    print(num, end=" ")

# printing the even numbvers form the lsit
for num in list_1:
    if num % 2 == 0:
        print(num, end=" ")

# sum of the elements in the list
sum = 0
for num in list_1:
    sum += num
print(sum)

list2 = [(2, 4), (6, 8), (10, 12)]
list3 = []
for num1, num2 in list2:
    list3.append(num1 + num2)
print(list3)

list2 = [[1, 2], [2, 3], [4, 5]]
for num1, num2 in list2:
    print(num1 + num2, end=" ")

# using for loops on a dictionary
d = {"k1": 1, "k2": 2, "k3": 3}
for item in d:
    print(item, end=" ")

for keys in d.keys():
    print(keys, end=" ")

for values in d.values():
    print(values, end=" ")

for key, value in d.items():
    print(key, value)
