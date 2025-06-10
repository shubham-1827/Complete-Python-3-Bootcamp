print("Welcome to list generator and manipulator!!!!")

from random import randint
from types import NoneType


def generate_list():
    lst = []
    is_generated = False
    while is_generated == False:
        choice = input(
            "Want to generate a list on your own with index and values or want a list with random nums, 1 or 2 : "
        )
        if choice not in ["1", "2"]:
            print("Try again good sir, remember 1 or 2")
            continue

        if int(choice) == 1:
            lst = list(input("Enter the elements seperated by , : ").split(", "))
            # this will convert all the list elements to integer
            lst = list(map(int, lst))
            is_generated = True
        if int(choice) == 2:
            elements = int(input("Enter the elements to add to the list : "))
            random_range = list(
                input("Enter the range of random numbers to add : ").split(", ")
            )
            lst = [
                randint(int(random_range[0]), int(random_range[1]))
                for _ in range(elements)
            ]
            is_generated = True
    return lst


def print_lst(lst):
    print(lst)


def manipulate_list(lst=[]):
    if lst == []:
        generate_list()
    print("This is your Current list : ")
    print_lst(lst)
    print("\n")

    is_manipulated = False
    while not is_manipulated:
        idx = input(f"Enter the index in range 0 to {len(lst) - 1} : ")
        if not idx.isdigit() or int(idx) not in range(len(lst)):
            print("You entered the wrong index, try again!!!!!")
            continue
        int_idx = int(idx)
        change_value = input("Enter the value to change to : ")
        if change_value.isdigit():
            lst[int_idx] = int(change_value)
        elif change_value.isdecimal():
            lst[int_idx] = float(change_value)
        else:
            lst[int_idx] = change_value

        print("\n")
        print("The final list after the changes : ")
        print_lst(lst)
        print("\n")

        choice = input("Want to keep continuing (Y or N) : ")
        if choice.lower() == "n":
            is_manipulated = True


manipulate_list()
