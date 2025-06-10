# list comprehensions in python are the quicker ways to create a list
# all the things you can do using  list comprehensions, you can also easily do with for loop
# it is jsut a more fancier method
lst = [x for x in "shubham"]
print(lst)

squares = [x**2 for x in range(0, 11)]
print(squares)

# lets check for even numbers in range
# if single if statement then it goes to the end
evens = [x for x in range(0, 51) if x % 2 == 0]
# if both if else are there then it comes to the from of for loop
evens_odds = [x if x % 2 == 0 else "odd" for x in range(0, 51)]
print(evens)
print(evens_odds)

# clesius to fehrenhite convertor
celcius_lst = list(range(0, 51))
print(celcius_lst)
fehr_lst = [((9 / 5) * temp + 32) for temp in celcius_lst]
print(fehr_lst)

# nested list comprehension
# lets generate x^4 elements till x = 0 to 10
lst = [x**2 for x in [x**2 for x in range(11)]]
print(lst)
