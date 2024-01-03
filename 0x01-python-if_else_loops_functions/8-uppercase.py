#!/usr/bin/python3

def uppercase(s):
    result = ""
    for char in s:
        ascii_value = ord(char)
        if 97 <= ascii_value <= 122:
            ascii_value -= 32
        result += "{:c}".format(ascii_value)
    print(result)  # Print the modified string

# Test cases
uppercase("best")
uppercase("Best School 98 Battery street")
uppercase("Holberton")
uppercase("Holberton School")
uppercase("Holberton School, 98 battery street")
uppercase("")
uppercase(98)
uppercase("z")
