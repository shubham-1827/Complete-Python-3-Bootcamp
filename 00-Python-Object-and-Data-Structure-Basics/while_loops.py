# while loops are used when you want to repeat a block of code until a certain condition is met.

x = 0
while x < 10:
    print(f"the current value of x is {x}")
    x += 1
else:
    print("the while loops is complete")


# Check if a number is prime or not
def is_prime(num):
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    else:
        return True


is_prime(5)
