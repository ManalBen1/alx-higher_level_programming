#!/usr/bin/python3

# Define variables a and b
a = 1
b = 2

# Execute the contents of add_0.py using exec and compile
exec(compile(open("add_0.py").read(), "add_0.py", 'exec'), globals())

# Call the add function and store the result
result = add(a, b)

# Print the result using string formatting
print("{} + {} = {}".format(a, b, result))
