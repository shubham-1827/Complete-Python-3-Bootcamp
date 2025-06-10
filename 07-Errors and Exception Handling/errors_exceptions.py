for i in ["a", "b", "c"]:
    try:
        print(i**2)
    except TypeError:
        print("The i is a string, not an integer, so can't power it up!!!")


x = 5
y = 0

try:
    x = x / y
except ZeroDivisionError:
    print("Hey my guy, you are dividing by zero!!!!, stop it get some help -----")
finally:
    print("All done!!!")


def ask():
    while True:
        try:
            number = int(input("Enter a number to get a square : "))
        except ValueError:
            print("Enter an integer bro, nothing else!!!")
            print("Try again ... ")
            continue
        else:
            print(f"Thank You, the square of {number} is {number ** 2}")
            break


ask()
