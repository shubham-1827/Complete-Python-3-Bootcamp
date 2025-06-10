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
# # Statements Assessment Test
# Let's test your knowledge!

# %% [markdown]
# _____
# **Use <code>for</code>, .split(), and <code>if</code> to create a Statement that will print out words that start with 's':**

# %%
st = "Print only the words that start with s in this sentence"

# %%
# Code here
st = st.split()
for word in st:
    if word[0] == "s":
        print(word)

# %% [markdown]
# ______
# **Use range() to print all the even numbers from 0 to 10.**

# %%
# Code Here
print(list(range(0, 11, 2)))

# %% [markdown]
# ___
# **Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.**

# %%
# Code in this cell
lst = [x for x in range(1, 51) if x % 3 == 0]
print(lst)

# %% [markdown]
# _____
# **Go through the string below and if the length of a word is even print "even!"**

# %%
st = "Print every word in this sentence that has an even number of letters"

# %%
# Code in this cell
st = st.split()
for word in st:
    if len(word) % 2 == 0:
        print(word)

# %% [markdown]
# ____
# **Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".**

# %%
# Code in this cell
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# using list Comprehension
lst = [
    "FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i
    for i in range(1, 101)
]
print(lst)
# %% [markdown]
# ____
# **Use List Comprehension to create a list of the first letters of every word in the string below:**

# %%
st = "Create a list of the first letters of every word in this string"

# %%
# Code in this cell
first_letters = [word[0] for word in st.split()]
print(first_letters)

# %% [markdown]
# ### Great Job!
