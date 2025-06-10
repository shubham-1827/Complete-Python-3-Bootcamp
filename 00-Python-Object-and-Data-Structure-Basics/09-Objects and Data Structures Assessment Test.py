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
# # Objects and Data Structures Assessment Test

# %% [markdown]
# ## Test your knowledge.
#
# ** Answer the following questions **

# %% [markdown]
# Write (or just say out loud to yourself) a brief description of all the following Object Types and Data Structures we've learned about. You can edit the cell below by double clicking on it. Really this is just to test if you know the difference between these, so feel free to just think about it, since your answers are self-graded.

# %% [markdown]
# Double Click HERE to edit this markdown cell and write answers.
#
# Numbers:
#
# Strings:
#
# Lists:
#
# Tuples:
#
# Dictionaries:
#

# %% [markdown]
# ## Numbers
#
# Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
equation = 50 * 2 + 0.25
print(equation)
#
# Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25

# %%

# %% [markdown]
# Answer these 3 questions without typing code. Then type code to check your answer.
#
#     What is the value of the expression 4 * (6 + 5) -> 44
#
#     What is the value of the expression 4 * 6 + 5 -> 29
#
#     What is the value of the expression 4 + 6 * 5 -> 34

# %%

# %% [markdown]
# What is the *type* of the result of the expression 3 + 1.5 + 4?<br><br>
print(type(3 + 1.5 + 4))  # the type will be float

# %% [markdown]
# What would you use to find a number’s square root, as well as its square?
# n = int(input("Enter a number : "))
n = 4
square = n**2
underroot = n**0.5
print(square, underroot)
# %%
# Square root:


# %%
# Square:


# %% [markdown]
# ## Strings

# %% [markdown]
# Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:

# %%
s = "hello"
# Print out 'e' using indexing
print(s[1])


# %% [markdown]
# Reverse the string 'hello' using slicing:

# %%
s = "hello"
# Reverse the string using slicing
print(s[::-1])


# %% [markdown]
# Given the string hello, give two methods of producing the letter 'o' using indexing.

# %%
s = "hello"
# Print out the 'o'

# Method 1:
print(s[-1])

# %%
# Method 2:
print(s[len(s) - 1])

# %% [markdown]
# ## Lists

# %% [markdown]
# Build this list [0,0,0] two separate ways.

# %%
# Method 1:
list_1 = [0, 0, 0]


# %%
# Method 2:
list_1 = [0]
list_1 *= 3
print(list_1)

# %% [markdown]
# Reassign 'hello' in this nested list to say 'goodbye' instead:

# %%
list3 = [1, 2, [3, 4, "hello"]]
list3[-1][-1] = "goodbye"
print(list3)


# %% [markdown]
# Sort the list below:

# %%
list4 = [5, 3, 4, 6, 1]
list4.sort()
print(list4)


# %% [markdown]
# ## Dictionaries

# %% [markdown]
# Using keys and indexing, grab the 'hello' from the following dictionaries:

# %%
d = {"simple_key": "hello"}
# Grab 'hello'
print(d["simple_key"])

# %%
d = {"k1": {"k2": "hello"}}
# Grab 'hello'
print(d["k1"]["k2"])


# %%
# Getting a little tricker
d = {"k1": [{"nest_key": ["this is deep", ["hello"]]}]}
# Grab hello
print(d["k1"][0]["nest_key"][1][0])


# %%
# This will be hard and annoying!
d = {"k1": [1, 2, {"k2": ["this is tricky", {"tough": [1, 2, ["hello"]]}]}]}
# grab hello
print(d["k1"][2]["k2"][1]["tough"][2][0])

# %% [markdown]
# Can you sort a dictionary? Why or why not?<br><br>
print(
    "no you cant sort a dictionary, because it is assigned by the key value pairs, and if you want some thing soreted then go for lists you mother fucker why dictionary ?"
)

# %% [markdown]
# ## Tuples

# %% [markdown]
# What is the major difference between tuples and lists?<br><br>
print(
    "tuples are immutable and has very few methods only count and index, and list is just opposite muttable and lots of methods to use..."
)

# %% [markdown]
# How do you create a tuple?<br><br>
t = (1, 2, 3)
print(type(t))

# %% [markdown]
# ## Sets

# %% [markdown]
# What is unique about a set?<br><br>
print("set only stores the uniques elements")

# %% [markdown]
# Use a set to find the unique values of the list below:

# %%
list5 = [1, 2, 2, 33, 4, 4, 11, 22, 3, 3, 2]
print(set(list5))


# %% [markdown]
# ## Booleans

# %% [markdown]
# For the following quiz questions, we will get a preview of comparison operators. In the table below, a=3 and b=4.
#
# <table class="table table-bordered">
# <tr>
# <th style="width:10%">Operator</th><th style="width:45%">Description</th><th>Example</th>
# </tr>
# <tr>
# <td>==</td>
# <td>If the values of two operands are equal, then the condition becomes true.</td>
# <td> (a == b) is not true.</td>
# </tr>
# <tr>
# <td>!=</td>
# <td>If values of two operands are not equal, then condition becomes true.</td>
# <td> (a != b) is true.</td>
# </tr>
# <tr>
# <td>&gt;</td>
# <td>If the value of left operand is greater than the value of right operand, then condition becomes true.</td>
# <td> (a &gt; b) is not true.</td>
# </tr>
# <tr>
# <td>&lt;</td>
# <td>If the value of left operand is less than the value of right operand, then condition becomes true.</td>
# <td> (a &lt; b) is true.</td>
# </tr>
# <tr>
# <td>&gt;=</td>
# <td>If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.</td>
# <td> (a &gt;= b) is not true. </td>
# </tr>
# <tr>
# <td>&lt;=</td>
# <td>If the value of left operand is less than or equal to the value of right operand, then condition becomes true.</td>
# <td> (a &lt;= b) is true. </td>
# </tr>
# </table>

# %% [markdown]
# What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)

# %%
# Answer before running cell
2 > 3  # false

# %%
# Answer before running cell
3 <= 2  # false

# %%
# Answer before running cell
3 == 2.0  # false

# %%
# Answer before running cell
3.0 == 3  # true

# %%
# Answer before running cell
4**0.5 != 2  # false

# %% [markdown]
# Final Question: What is the boolean output of the cell block below?

# %%
# two nested lists
l_one = [1, 2, [3, 4]]
l_two = [1, 2, {"k1": 4}]

# True or False?
l_one[2][0] >= l_two[2]["k1"]  # false

# %% [markdown]
# ## Great Job on your first assessment!
