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
# # Object Oriented Programming Challenge
#
# For this challenge, create a bank account class that has two attributes:
#
# * owner
# * balance
#
# and two methods:
#
# * deposit
# * withdraw
#
# As an added requirement, withdrawals may not exceed the available balance.
#
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.


# %%
class Account:
    pass


# %%
# 1. Instantiate the class
acct1 = Account("Jose", 100)

# %%
# 2. Print the object
print(acct1)

# %%
# 3. Show the account owner attribute
acct1.owner

# %%
# 4. Show the account balance attribute
acct1.balance

# %%
# 5. Make a series of deposits and withdrawals
acct1.deposit(50)

# %%
acct1.withdraw(75)

# %%
# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)

# %% [markdown]
# ## Good job!
