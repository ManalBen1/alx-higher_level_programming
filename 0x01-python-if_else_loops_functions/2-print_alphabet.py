#!/usr/bin/python3

for letter in range(ord('a'), ord('z')+1):
    print("{}".format(chr(letter)), end="" if letter != ord('z') else "\n")
