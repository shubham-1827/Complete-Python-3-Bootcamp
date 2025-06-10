# adding the elements of the lists using map
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = list(map(lambda x, y: x + y, lst1, lst2))

# can be extended for any number of lists
lst4 = list(map(lambda x, y, z: x + y + z, lst1, lst2, lst3))
print(lst4)


# function to find the length of each word in a phrase
def word_lengths(phrase: str) -> list:
    return list(map(len, phrase.split()))


print(word_lengths("Shubham is a good student, and he is very very smart"))

# fuction to convert a list of number to its equivalent digit
# like [1,3,4] -> 134

import enum
from typing import List
from functools import reduce


# using reduce write a function to sum all the values in a list
def sum(lst: list) -> int:
    return reduce(lambda x, y: x + y, lst)


print(sum([1, 2, 3, 4, 5, 6, 7, 8]))


# first way convert to string and then reconvert to int
def digits_to_num(lst: List[int]) -> int:
    return reduce(lambda x, y: x * 10 + y, lst)


print(digits_to_num([3, 4, 3, 2, 1]))


# a function which returns true if the words in a phrase starts with a target letter
def filter_words(phrase: str, letter: str):
    return list(filter(lambda x: x[0] == letter, phrase.split()))


print(filter_words("shubham is a good guy", "g"))


# Use zip() and a list comprehension to return a list of the same length where each value is the two strings from L1 and L2 concatenated together with connector between them.
def concatenate(l1: List, l2: List, connector: str) -> List:
    return list(map(connector.join, list(zip(l1, l2))))


print(concatenate(l1 := ["A", "B"], l2 := ["a", "b"], "-"))
print(l1)
print(l2)

# Use enumerate() and other skills to return a dictionary which has the values of the list as keys and the index as the value.


def d_list(lst: list) -> dict:
    d = {}
    for idx, val in enumerate(lst):
        d[val] = idx
    return d


print(d_list(["a", "b", "c", "d"]))

# Use enumerate() and other skills from above to return the count of the number of items in the list whose value equals its index.


def count_match_index(lst: list) -> int:
    return len(list(filter(lambda x: x[0] == x[1], enumerate(lst))))


print(count_match_index([0, 2, 2, 1, 5, 5, 6, 10]))

# using the start attribute in enumerate()
# the start attribute sets the starting point of enumerate function
lst1 = ["march", "april", "may", "june"]
for values, months in enumerate(lst1, start=3):
    print(f"{months} : {values}")
