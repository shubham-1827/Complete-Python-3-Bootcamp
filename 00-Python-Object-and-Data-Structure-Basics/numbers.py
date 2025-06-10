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
# # Numbers and more in Python!
#
# In this lecture, we will learn about numbers in Python and how to use them.
#
# We'll learn about the following topics:
#
#     1.) Types of Numbers in Python
#     2.) Basic Arithmetic
#     3.) Differences between classic division and floor division
#     4.) Object Assignment in Python

# %% [markdown]
# ## Types of numbers
#
# Python has various "types" of numbers (numeric literals). We'll mainly focus on integers and floating point numbers.
#
# Integers are just whole numbers, positive or negative. For example: 2 and -2 are examples of integers.
#
# Floating point numbers in Python are notable because they have a decimal point in them, or use an exponential (e) to define the number. For example 2.0 and -2.1 are examples of floating point numbers. 4E2 (4 times 10 to the power of 2) is also an example of a floating point number in Python.
#
# Throughout this course we will be mainly working with integers or simple float number types.
#
# Here is a table of the two main types we will spend most of our time working with some examples:

# %% [markdown]
# <table>
# <tr>
#     <th>Examples</th> 
#     <th>Number "Type"</th>
# </tr>
#
# <tr>
#     <td>1,2,-5,1000</td>
#     <td>Integers</td> 
# </tr>
#
# <tr>
#     <td>1.2,-0.5,2e2,3E2</td> 
#     <td>Floating-point numbers</td> 
# </tr>
#  </table>

# %% [markdown]
#  
#  
# Now let's start with some basic arithmetic.

# %% [markdown]
# ### Basic Arithmetic

# %%
# Addition
2+1

# %%
# Subtraction
2-1

# %%
# Multiplication
2*2

# %%
# Division
3/2

# %%
# Floor Division
7//4

# %% [markdown]
# **Whoa! What just happened? Last time I checked, 7 divided by 4 equals 1.75 not 1!**
#
# The reason we get this result is because we are using "*floor*" division. The // operator (two forward slashes) truncates the decimal without rounding, and returns an integer result.

# %% [markdown]
# **So what if we just want the remainder after division?**

# %%
# Modulo
7%4

# %% [markdown]
# 4 goes into 7 once, with a remainder of 3. The % operator returns the remainder after division.

# %% [markdown]
# ### Arithmetic continued

# %%
# Powers
2**3

# %%
# Can also do roots this way
4**0.5

# %%
# Order of Operations followed in Python
2 + 10 * 10 + 3

# %%
# Can use parentheses to specify orders
(2+10) * (10+3)

# %% [markdown]
# ## Variable Assignments
#
# Now that we've seen how to use numbers in Python as a calculator let's see how we can assign names and create variables.
#
# We use a single equals sign to assign labels to variables. Let's see a few examples of how we can do this.

# %%
# Let's create an object called "a" and assign it the number 5
a = 5

# %% [markdown]
# Now if I call *a* in my Python script, Python will treat it as the number 5.

# %%
# Adding the objects
a+a

# %% [markdown]
# What happens on reassignment? Will Python let us write it over?

# %%
# Reassignment
a = 10

# %%
# Check
a

# %% [markdown]
# Yes! Python allows you to write over assigned variable names. We can also use the variables themselves when doing the reassignment. Here is an example of what I mean:

# %%
# Check
a

# %%
# Use A to redefine A
a = a + a

# %%
# Check 
a

# %% [markdown]
# The names you use when creating these labels need to follow a few rules:
#
#     1. Names can not start with a number.
#     2. There can be no spaces in the name, use _ instead.
#     3. Can't use any of these symbols :'",<>/?|\()!@#$%^&*~-+
#     4. It's considered best practice (PEP8) that names are lowercase.
#     5. Avoid using the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), 
#        or 'I' (uppercase letter eye) as single character variable names.
#     6. Avoid using words that have special meaning in Python like "list" and "str"
#
#
# Using variable names can be a very useful way to keep track of different variables in Python. For example:

# %%
# Use object names to keep better track of what's going on in your code!
my_income = 100

tax_rate = 0.1

my_taxes = my_income*tax_rate

# %%
# Show my taxes!
my_taxes

# %% [markdown]
# So what have we learned? We learned some of the basics of numbers in Python. We also learned how to do arithmetic and use Python as a basic calculator. We then wrapped it up with learning about Variable Assignment in Python.
#
# Up next we'll learn about Strings!
