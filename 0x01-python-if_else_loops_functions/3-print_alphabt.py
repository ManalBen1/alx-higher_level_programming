#!/usr/bin/python3

for letter in range(ord('a'), ord('z') + 1):
    if chr(letter) not in ['q', 'e']:
        print("{:s}".format(chr(letter)), end="")

# No newline character is added to match the expected output
