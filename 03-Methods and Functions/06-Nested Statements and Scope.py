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
# # Nested Statements and Scope 
#
# Now that we have gone over writing our own functions, it's important to understand how Python deals with the variable names you assign. When you create a variable name in Python the name is stored in a *name-space*. Variable names also have a *scope*, the scope determines the visibility of that variable name to other parts of your code.
#
# Let's start with a quick thought experiment; imagine the following code:

# %%
x = 25

def printer():
    x = 50
    return x

# print(x)
# print(printer())


# %% [markdown]
# What do you imagine the output of printer() is? 25 or 50? What is the output of print x? 25 or 50?

# %%
print(x)

# %%
print(printer())

# %% [markdown]
# Interesting! But how does Python know which **x** you're referring to in your code? This is where the idea of scope comes in. Python has a set of rules it follows to decide what variables (such as **x** in this case) you are referencing in your code. Lets break down the rules:

# %% [markdown]
# This idea of scope in your code is very important to understand in order to properly assign and call variable names. 
#
# In simple terms, the idea of scope can be described by 3 general rules:
#
# 1. Name assignments will create or change local names by default.
# 2. Name references search (at most) four scopes, these are:
#     * local
#     * enclosing functions
#     * global
#     * built-in
# 3. Names declared in global and nonlocal statements map assigned names to enclosing module and function scopes.
#
#
# The statement in #2 above can be defined by the LEGB rule.
#
# **LEGB Rule:**
#
# L: Local — Names assigned in any way within a function (def or lambda), and not declared global in that function.
#
# E: Enclosing function locals — Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer.
#
# G: Global (module) — Names assigned at the top-level of a module file, or declared global in a def within the file.
#
# B: Built-in (Python) — Names preassigned in the built-in names module : open, range, SyntaxError,...

# %% [markdown]
# ## Quick examples of LEGB
#
# ### Local

# %%
# x is local here:
f = lambda x:x**2

# %% [markdown]
# ### Enclosing function locals
# This occurs when we have a function inside a function (nested functions)
#

# %%
name = 'This is a global name'

def greet():
    # Enclosing function
    name = 'Sammy'
    
    def hello():
        print('Hello '+name)
    
    hello()

greet()

# %% [markdown]
# Note how Sammy was used, because the hello() function was enclosed inside of the greet function!

# %% [markdown]
# ### Global
# Luckily in Jupyter a quick way to test for global variables is to see if another cell recognizes the variable!

# %%
print(name)

# %% [markdown]
# ### Built-in
# These are the built-in function names in Python (don't overwrite these!)

# %%
len

# %% [markdown]
# ## Local Variables
# When you declare variables inside a function definition, they are not related in any way to other variables with the same names used outside the function - i.e. variable names are local to the function. This is called the scope of the variable. All variables have the scope of the block they are declared in starting from the point of definition of the name.
#
# Example:

# %%
x = 50

def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)

func(x)
print('x is still', x)

# %% [markdown]
# The first time that we print the value of the name **x** with the first line in the function’s body, Python uses the value of the parameter declared in the main block, above the function definition.
#
# Next, we assign the value 2 to **x**. The name **x** is local to our function. So, when we change the value of **x** in the function, the **x** defined in the main block remains unaffected.
#
# With the last print statement, we display the value of **x** as defined in the main block, thereby confirming that it is actually unaffected by the local assignment within the previously called function.
#
# ## The <code>global</code> statement
# If you want to assign a value to a name defined at the top level of the program (i.e. not inside any kind of scope such as functions or classes), then you have to tell Python that the name is not local, but it is global. We do this using the <code>global</code> statement. It is impossible to assign a value to a variable defined outside a function without the global statement.
#
# You can use the values of such variables defined outside the function (assuming there is no variable with the same name within the function). However, this is not encouraged and should be avoided since it becomes unclear to the reader of the program as to where that variable’s definition is. Using the <code>global</code> statement makes it amply clear that the variable is defined in an outermost block.
#
# Example:

# %%
x = 50

def func():
    global x
    print('This function is now using the global x!')
    print('Because of global x is: ', x)
    x = 2
    print('Ran func(), changed global x to', x)

print('Before calling func(), x is: ', x)
func()
print('Value of x (outside of func()) is: ', x)

# %% [markdown]
# The <code>global</code> statement is used to declare that **x** is a global variable - hence, when we assign a value to **x** inside the function, that change is reflected when we use the value of **x** in the main block.
#
# You can specify more than one global variable using the same global statement e.g. <code>global x, y, z</code>.

# %% [markdown]
# ## Conclusion
# You should now have a good understanding of Scope (you may have already intuitively felt right about Scope which is great!) One last mention is that you can use the **globals()** and **locals()** functions to check what are your current local and global variables.
#
# Another thing to keep in mind is that everything in Python is an object! I can assign variables to functions just like I can with numbers! We will go over this again in the decorator section of the course!
