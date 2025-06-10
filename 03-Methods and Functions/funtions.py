# lets create a red ball guessing game from the three cups

# a function to shuffle the list
from random import shuffle


def shuffle_list(lst):
    shuffle(lst)
    return lst


def guess():
    num = int(input("Enter a Number between, 0, 1, and 2 : "))
    return num


def guessing_game():
    lst = ["", "O", ""]
    lst = shuffle_list(lst)
    while True:
        g = guess()
        if lst[g] == "O":
            print("Yoooo, you win the game")
            break
        else:
            print("try again!!!!")
            lst = shuffle_list(lst)


guessing_game()
