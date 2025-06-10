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
# # Decorators
#
#
# Decorators can be thought of as functions which modify the *functionality* of another function. They help to make your code shorter and more "Pythonic". 
#
# To properly explain decorators we will slowly build up from functions. Make sure to run every cell in this Notebook for this lecture to look the same on your own computer.<br><br>So let's break down the steps:
#
# ## Functions Review

# %%
def func():
    return 1


# %%
func()

# %% [markdown]
# ## Scope Review
# Remember from the nested statements lecture that Python uses Scope to know what a label is referring to. For example:

# %%
s = 'Global Variable'

def check_for_locals():
    print(locals())


# %% [markdown]
# Remember that Python functions create a new scope, meaning the function has its own namespace to find variable names when they are mentioned within the function. We can check for local variables and global variables with the <code>locals()</code> and <code>globals()</code> functions. For example:

# %%
print(globals())

# %% [markdown]
# Here we get back a dictionary of all the global variables, many of them are predefined in Python. So let's go ahead and look at the keys:

# %%
print(globals().keys())

# %% [markdown]
# Note how **s** is there, the Global Variable we defined as a string:

# %%
globals()['s']

# %% [markdown]
# Now let's run our function to check for local variables that might exist inside our function (there shouldn't be any)

# %%
check_for_locals()


# %% [markdown]
# Great! Now lets continue with building out the logic of what a decorator is. Remember that in Python **everything is an object**. That means functions are objects which can be assigned labels and passed into other functions. Lets start with some simple examples:

# %%
def hello(name='Jose'):
    return 'Hello '+name


# %%
hello()

# %% [markdown]
# Assign another label to the function. Note that we are not using parentheses here because we are not calling the function **hello**, instead we are just passing a function object to the **greet** variable.

# %%
greet = hello

# %%
greet

# %%
greet()

# %% [markdown]
# So what happens when we delete the name **hello**?

# %%
del hello

# %%
hello()

# %%
greet()


# %% [markdown]
# Even though we deleted the name **hello**, the name **greet** *still points to* our original function object. It is important to know that functions are objects that can be passed to other objects!

# %% [markdown]
# ## Functions within functions
# Great! So we've seen how we can treat functions as objects, now let's see how we can define functions inside of other functions:

# %%
def hello(name='Jose'):
    print('The hello() function has been executed')
    
    def greet():
        return '\t This is inside the greet() function'
    
    def welcome():
        return "\t This is inside the welcome() function"
    
    print(greet())
    print(welcome())
    print("Now we are back inside the hello() function")


# %%
hello()

# %%
welcome()


# %% [markdown]
# Note how due to scope, the welcome() function is not defined outside of the hello() function. Now lets learn about returning functions from within functions:
# ## Returning Functions

# %%
def hello(name='Jose'):
    
    def greet():
        return '\t This is inside the greet() function'
    
    def welcome():
        return "\t This is inside the welcome() function"
    
    if name == 'Jose':
        return greet
    else:
        return welcome


# %% [markdown]
# Now let's see what function is returned if we set x = hello(), note how the empty parentheses means that name has been defined as Jose.

# %%
x = hello()

# %%
x

# %% [markdown]
# Great! Now we can see how x is pointing to the greet function inside of the hello function.

# %%
print(x())


# %% [markdown]
# Let's take a quick look at the code again. 
#
# In the <code>if</code>/<code>else</code> clause we are returning <code>greet</code> and <code>welcome</code>, not <code>greet()</code> and <code>welcome()</code>. 
#
# This is because when you put a pair of parentheses after it, the function gets executed; whereas if you don’t put parentheses after it, then it can be passed around and can be assigned to other variables without executing it.
#
# When we write <code>x = hello()</code>, hello() gets executed and because the name is Jose by default, the function <code>greet</code> is returned. If we change the statement to <code>x = hello(name = "Sam")</code> then the <code>welcome</code> function will be returned. We can also do <code>print(hello()())</code> which outputs *This is inside the greet() function*.

# %% [markdown]
# ## Functions as Arguments
# Now let's see how we can pass functions as arguments into other functions:

# %%
def hello():
    return 'Hi Jose!'

def other(func):
    print('Other code would go here')
    print(func())


# %%
other(hello)


# %% [markdown]
# Great! Note how we can pass the functions as objects and then use them within other functions. Now we can get started with writing our first decorator:

# %% [markdown]
# ## Creating a Decorator
# In the previous example we actually manually created a Decorator. Here we will modify it to make its use case clear:

# %%
def new_decorator(func):

    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func

def func_needs_decorator():
    print("This function is in need of a Decorator")


# %%
func_needs_decorator()

# %%
# Reassign func_needs_decorator
func_needs_decorator = new_decorator(func_needs_decorator)

# %%
func_needs_decorator()


# %% [markdown]
# So what just happened here? A decorator simply wrapped the function and modified its behavior. Now let's understand how we can rewrite this code using the @ symbol, which is what Python uses for Decorators:

# %%
@new_decorator
def func_needs_decorator():
    print("This function is in need of a Decorator")


# %%
func_needs_decorator()

# %% [markdown]
# **Great! You've now built a Decorator manually and then saw how we can use the @ symbol in Python to automate this and clean our code. You'll run into Decorators a lot if you begin using Python for Web Development, such as Flask or Django!**
