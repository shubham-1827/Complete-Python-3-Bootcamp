# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# ___
#
# <a href='https://www.udemy.com/user/joseportilla/'><img src='../Pierian_Data_Logo.png'/></a>
# ___
# <center><em>Content Copyright by Pierian Data</em></center>

# %% [markdown]
# # Functions and Methods Homework
#
# Complete the following questions:
# ____
# **Write a function that computes the volume of a sphere given its radius.**
# <p>The volume of a sphere is given as $$\frac{4}{3} πr^3$$</p>

# %%
from contextlib import ContextDecorator


def vol(rad):
    PI = 3.1415
    return (4 / 3) * PI * (rad**3)


# %%
# Check
vol(2)

# %% [markdown]
# ___
# **Write a function that checks whether a number is in a given range (inclusive of high and low)**


# %%
def ran_check(num, low, high):
    if num >= low and num <= high:
        print(f"{num} is in range {low} to {high}")
        return
    print(f"{num} is out of range....")


# %%
# Check
ran_check(5, 2, 7)


# %% [markdown]
# If you only wanted to return a boolean:


# %%
def ran_bool(num, low, high):
    if num >= low and num <= high:
        return True
    return False


# %%
ran_bool(3, 1, 10)


# %% [markdown]
# ____
# **Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.**
#
#     Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
#     Expected Output :
#     No. of Upper case characters : 4
#     No. of Lower case Characters : 33
#
# HINT: Two string methods that might prove useful: **.isupper()** and **.islower()**
#
# If you feel ambitious, explore the Collections module to solve this problem!


# %%
def up_low(s: str):
    count_up = 0
    count_low = 0
    for word in s:
        for letter in word:
            if letter.isupper():
                count_up += 1
            elif letter.islower():
                count_low += 1
    print(f"No. of upper case letters : {count_up}")
    print(f"No. of lower case letters : {count_low}")


# %%
s = "Hello Mr. Rogers, how are you this fine Tuesday?"
type(s)
up_low(s)


# %% [markdown]
# ____
# **Write a Python function that takes a list and returns a new list with unique elements of the first list.**
#
#     Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
#     Unique List : [1, 2, 3, 4, 5]


# %%
def unique_list(lst):
    return list(set(lst))


# %%
unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5])


# %% [markdown]
# ____
# **Write a Python function to multiply all the numbers in a list.**
#
#     Sample List : [1, 2, 3, -4]
#     Expected Output : -24

# %%
from typing import List


def multiply(numbers: List[int]):
    res = 1
    for num in numbers:
        res *= num
    return res


# %%
multiply([1, 2, 3, -4])


# %% [markdown]
# ____
# **Write a Python function that checks whether a word or phrase is palindrome or not.**
#
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run". Hint: You may want to check out the .replace() method in a string to help out with dealing with spaces. Also google search how to reverse a string in Python, there are some clever ways to do it with slicing notation.


# %%
def palindrome(s: str):
    s = s.replace(" ", "")
    if s == s[::-1]:
        return True
    return False


# %%
palindrome("helleh")
palindrome("nurses run")
palindrome("shubham")
# %% [markdown]
# ____
# #### Hard:
#
# **Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)**
#
#     Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
#     For example : "The quick brown fox jumps over the lazy dog"
#
# Hint: You may want to use .replace() method to get rid of spaces.
#
# Hint: Look at the [string module](https://stackoverflow.com/questions/16060899/alphabet-range-in-python)
#
# Hint: In case you want to use [set comparisons](https://medium.com/better-programming/a-visual-guide-to-set-comparisons-in-python-6ab7edb9ec41)

# %%
import string


def ispangram(str1, alphabet=string.ascii_lowercase):
    alphabet = set(alphabet)
    str1 = set(str1.replace(" ", ""))
    if alphabet.intersection(str1) == alphabet:
        return True
    return False


# another more pythony way
def ispangram(str1, alphabet=string.ascii_lowercase):
    return set(alphabet).issubset(str1.lower())


ispangram("shubham")


# %%
ispangram("The quick brown fox jumps over the lazy dog")

# %%
string.ascii_lowercase

# %% [markdown]
# #### Great Job!
