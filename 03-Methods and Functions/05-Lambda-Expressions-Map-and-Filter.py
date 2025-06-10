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
# # Lambda Expressions, Map, and Filter
#
# Now its time to quickly learn about two built in functions, filter and map. Once we learn about how these operate, we can learn about the lambda expression, which will come in handy when you begin to develop your skills further!

# %% [markdown]
# ## map function
#
# The **map** function allows you to "map" a function to an iterable object. That is to say you can quickly call the same function to every item in an iterable, such as a list. For example:


# %%
def square1(num):
    return num**2


# %%
my_nums = [1, 2, 3, 4, 5]

# %%
map(square1, my_nums)

# %%
# To get the results, either iterate through map()
# or just cast to a list
list(map(square1, my_nums))


# %% [markdown]
# The functions can also be more complex


# %%
def splicer(mystring):
    if len(mystring) % 2 == 0:
        return "even"
    else:
        return mystring[0]


# %%
mynames = ["John", "Cindy", "Sarah", "Kelly", "Mike"]

# %%
list(map(splicer, mynames))


# %% [markdown]
# ## filter function
#
# The filter function returns an iterator yielding those items of iterable for which function(item)
# is true. Meaning you need to filter by a function that returns either True or False. Then passing that into filter (along with your iterable) and you will get back only the results that would return True when passed to the function.


# %%
def check_even(num):
    return num % 2 == 0


# %%
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# %%
filter(check_even, nums)

# %%
list(filter(check_even, nums))


# %% [markdown]
# ## lambda expression
#
# One of Pythons most useful (and for beginners, confusing) tools is the lambda expression. lambda expressions allow us to create "anonymous" functions. This basically means we can quickly make ad-hoc functions without needing to properly define a function using def.
#
# Function objects returned by running lambda expressions work exactly the same as those created and assigned by defs. There is key difference that makes lambda useful in specialized roles:
#
# **lambda's body is a single expression, not a block of statements.**
#
# * The lambda's body is similar to what we would put in a def body's return statement. We simply type the result as an expression instead of explicitly returning it. Because it is limited to an expression, a lambda is less general that a def. We can only squeeze design, to limit program nesting. lambda is designed for coding simple functions, and def handles the larger tasks.

# %% [markdown]
# Lets slowly break down a lambda expression by deconstructing a function:


# %%
def square2(num):
    result = num**2
    return result


# %%
square2(2)


# %% [markdown]
# We could simplify it:


# %%
def square(num):
    return num**2


# %%
square(2)


# %% [markdown]
# We could actually even write this all on one line.


# %%
def square3(num):
    return num**2


# %%
square3(2)

# %% [markdown]
# This is the form a function that a lambda expression intends to replicate. A lambda expression can then be written as:

# %%
lambda num: num**2

# %%
# You wouldn't usually assign a name to a lambda expression, this is just for demonstration!
square = lambda num: num**2

# %%
square(2)

# %% [markdown]
# So why would use this? Many function calls need a function passed in, such as map and filter. Often you only need to use the function you are passing in once, so instead of formally defining it, you just use the lambda expression. Let's repeat some of the examples from above with a lambda expression

# %%
list(map(lambda num: num**2, my_nums))

# %%
list(filter(lambda n: n % 2 == 0, nums))

# %% [markdown]
# Here are a few more examples, keep in mind the more comples a function is, the harder it is to translate into a lambda expression, meaning sometimes its just easier (and often the only way) to create the def keyword function.

# %% [markdown]
# ** Lambda expression for grabbing the first character of a string: **

# %%
lambda s: s[0]

# %% [markdown]
# ** Lambda expression for reversing a string: **

# %%
lambda s: s[::-1]

# %% [markdown]
# You can even pass in multiple arguments into a lambda expression. Again, keep in mind that not every function can be translated into a lambda expression.

# %%
lambda x, y: x + y

# %% [markdown]
# You will find yourself using lambda expressions often with certain non-built-in libraries, for example the pandas library for data analysis works very well with lambda expressions.
