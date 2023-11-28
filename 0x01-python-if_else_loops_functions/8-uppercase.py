#!/usr/bin/python3
def uppercase(s):
    for char in s:
        uppercase_char = char if not ('a' <= char <= 'z')  else chr(ord(char) - ord('a') + ord('A'))

        print("{}".format(uppercase_char), end="")

    print()
