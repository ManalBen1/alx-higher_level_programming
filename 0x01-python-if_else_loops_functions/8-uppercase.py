#!/usr/bin/python3

def uppercase(s):
    for char in s:
        ascii_value = ord(char)
        if 97 <= ascii_value <= 122:
            ascii_value -= 32
        print("{:c}".format(ascii_value), end="")
    print()  # Print new line

# Test cases
uppercase("best")
uppercase("Best School 98 Battery street")
uppercase("Holberton")
