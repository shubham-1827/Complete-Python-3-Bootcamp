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
# # `*args` and `**kwargs`
#
# Work with Python long enough, and eventually you will encounter `*args` and `**kwargs`. These strange terms show up as parameters in function definitions. What do they do? Let's review a simple function:

# %%
def myfunc(a,b):
    return sum((a,b))*.05

myfunc(40,60)


# %% [markdown]
# This function returns 5% of the sum of **a** and **b**. In this example, **a** and **b** are *positional* arguments; that is, 40 is assigned to **a** because it is the first argument, and 60 to **b**. Notice also that to work with multiple positional arguments in the `sum()` function we had to pass them in as a tuple.
#
# What if we want to work with more than two numbers? One way would be to assign a *lot* of parameters, and give each one a default value.

# %%
def myfunc(a=0,b=0,c=0,d=0,e=0):
    return sum((a,b,c,d,e))*.05

myfunc(40,60,20)


# %% [markdown]
# Obviously this is not a very efficient solution, and that's where `*args` comes in.
#
# ## `*args`
#
# When a function parameter starts with an asterisk, it allows for an *arbitrary number* of arguments, and the function takes them in as a tuple of values. Rewriting the above function:

# %%
def myfunc(*args):
    return sum(args)*.05

myfunc(40,60,20)


# %% [markdown]
# Notice how passing the keyword "args" into the `sum()` function did the same thing as a tuple of arguments.
#
# It is worth noting that the word "args" is itself arbitrary - any word will do so long as it's preceded by an asterisk. To demonstrate this:

# %%
def myfunc(*spam):
    return sum(spam)*.05

myfunc(40,60,20)


# %% [markdown]
# ## `**kwargs`
#
# Similarly, Python offers a way to handle arbitrary numbers of *keyworded* arguments. Instead of creating a tuple of values, `**kwargs` builds a dictionary of key/value pairs. For example:

# %%
def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print(f"My favorite fruit is {kwargs['fruit']}")  # review String Formatting and f-strings if this syntax is unfamiliar
    else:
        print("I don't like fruit")

myfunc(fruit='pineapple')

# %%
myfunc()


# %% [markdown]
# ## `*args` and `**kwargs` combined
#
# You can pass `*args` and `**kwargs` into the same function, but `*args` have to appear before `**kwargs`

# %%
def myfunc(*args, **kwargs):
    if 'fruit' and 'juice' in kwargs:
        print(f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        print(f"May I have some {kwargs['juice']} juice?")
    else:
        pass

myfunc('eggs','spam',fruit='cherries',juice='orange')

# %% [markdown]
# Placing keyworded arguments ahead of positional arguments raises an exception:

# %%
myfunc(fruit='cherries',juice='orange','eggs','spam')

# %% [markdown]
# As with "args", you can use any name you'd like for keyworded arguments - "kwargs" is just a popular convention.
#
# That's it! Now you should understand how `*args` and `**kwargs` provide the flexibilty to work with arbitrary numbers of arguments!

# %%
def greet(*args, **kwargs):
    if ('Shubham' in args) and ('greeting' in kwargs):
        print(f'{kwargs["greeting"]}, Shubham')
    else:
        print('get the fudge out of here!!!!!')

greet('Jatin', 'Shubham', 'Ayush', greeting='Hello', classes='12th')

# %%
# the below function returns the list of sqrts for the arguments passed
from math import sqrt

#first way using args
def square(*args):
    return [sqrt(num) for num in args]

lst1 = square(3,4,6,7,12,14,18,20)
print(lst1)


# %%
#another way using map function

#generating a random list
from random import randint
lst1 = [randint(0,100) for _ in range(21)]

print(list(map(sqrt, lst1)))
