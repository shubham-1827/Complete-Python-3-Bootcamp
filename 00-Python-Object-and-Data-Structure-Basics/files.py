test_file = open("./test.txt")

test_file.seek(0)
content = test_file.read()
print(content)
print(content.split())

test_file.seek(0)
lines = test_file.readlines()
print(lines)

test_file.seek(0)
test_file.close()

# when you open files with w+ the original content gets deleted
file = open("./test.txt", "w+")  # this gives us the read and write permissions
file.write("this is a new line ")
file.seek(0)
contents = file.read()
print(contents)
file.close()

# there is also a append mode with a or a+ if you also want to read the file
new_file = open("./test.txt", mode="a+")
new_file.write("\nthis is annother new line")
new_file.write("\nthis is yet another new line")

new_file.seek(0)
for line in new_file:
    print(line)
