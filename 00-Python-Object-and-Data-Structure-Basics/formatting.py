print("i am going to inject %s here." % "something")

print("My name is %s and her name is %s" % ("shubham", "shivani"))

x, y, z = "shubham", "adi", "anjali"
print(
    "My name is %s and my cousin brothers name is %s and my cousin sisters name is %s"
    % (x, y, z)
)

# there are many formats like %s, %r and %d
# %s just evaluated the expression and then place it in place of %s
print("will it be evaluated : %s" % (1 + 1 + 3))
print("this is a big %s gap" % "big\tbig")  # this tab will be expanded in %s

# %r returns the things as is
print("this is a big %r gap" % "big\tbig")  # this tab will not be expanded in %r

# %d converts the number to the intergers than returns
print("this 3.15 will be %d" % (3.15))  # this is place 3 in place of %d

# formating with floating point numbers
# here 3 is the number of digits minimum before decimal
# 2 is the number of digits or precision after the decimal
print("A floating point number : %3.2f" % (132.4356))

# multiple formatting
print(
    "this is a %s formatted string, which has these %3.4f kind of numbers and also a %r"
    % ("multiple", 321.223434, "bye")
)

# using the .format() method
# this is a more preffered way than the % notation
print("this is a string with an {}".format("insert"))
print("In a {1}, there was a {2}, who attacks the {0}".format("cat", "jungle", "fox"))
print(
    "In a {j}, there was a {f}, who attacks the {c}".format(
        c="cat", j="jungle", f="fox"
    )
)

# we can also reuse the inserted objects
print("A {p} saved is a {p} earned".format(p="penny"))

# the first one here is the position argument like if .format has 2 things then it will be 0 or 1
print("this is my big decimal number : {0:10.3f}".format(3214.335643))

# f strings
name = "shubham"
print(f"this is a string which has my {name}")

print(f"this is like %r : {name!r}")

num = 3234.24353
print(f"this is a floating point number : {num:{10}.{6}}")
# note that here {6} refers to the total number of digits in the number not only after decimals
# 10 is same as .format() digits before decimal point

# you can also use .format kind of syntax in fstrings
print(f"This is a .format LIke syntax : {num:10.4f}")
