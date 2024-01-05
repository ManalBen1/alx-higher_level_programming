#!/usr/bin/python3

# Define variables a and b
a = 10
b = 5

# Execute the contents of calculator_1.py using exec and compile
exec(compile(open("calculator_1.py").read(), "calculator_1.py", 'exec'), globals())

# Call the imported functions and store results
add_result = add(a, b)
sub_result = sub(a, b)
mul_result = mul(a, b)
div_result = div(a, b)

# Print the results
print(f"{a} + {b} = {add_result}")
print(f"{a} - {b} = {sub_result}")
print(f"{a} * {b} = {mul_result}")
print(f"{a} / {b} = {div_result}")
