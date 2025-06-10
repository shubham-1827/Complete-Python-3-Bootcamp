# NOTE using locals() and globals() you can get the dictionary of local and global varaibles in a scope

# decorators in python are like wrappers for a birthday gift
# decorators take functions as input and wrap some extra functionalities to it


def new_decorator(func):
    def wrapper():
        print("this thing executes before func() call")
        func()
        print("this thing executes after func() call")

    return wrapper


def func():
    print("This is the stuff of func()")


func()
func = new_decorator(func)
func()

# another more pythonic way to use decorators are using the @ symbol


@new_decorator
def func2():
    print("This is the stuff inside func2()")


func2()

# creating decorators for the functions with arguments


def greet_decorator(func):
    def wrapper1(name):
        func(name)
        if name == "Shubham":
            print(f"How are you {name}")
        else:
            print(f"Welcome to the House, {name}")

    return wrapper1


@greet_decorator
def greet(name: str):
    print(f"Hello! {name}")


greet("Shubham")


# you can create even more custom decorators like the one below
def greet_mode(mode: str):
    def greet_decorator(func):
        def wrapper1(name):
            func(name)
            if mode == "informal":
                print(f"How are you {name}")
            else:
                print(f"Welcome to the House, {name}")

        return wrapper1

    return greet_decorator


# @greet_mode("formal")
def greet1(name: str):
    print(f"hello, {name}")


# greet1("Shubham")

# one more cool stuff -> running a returend function from a decorator in another way
greet_mode("informal")(greet1)("Shubham")
