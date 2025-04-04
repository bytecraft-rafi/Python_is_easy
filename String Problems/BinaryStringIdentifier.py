# Write a Python program to check if a given string is binary string or not.

def binary_string(input_str):
    for i in input_str:
        if i not in '10':
            return False

    return True


input_str= input("Enter a string")


if binary_string(input_str):
    print(f"{input_str} is a binary string")
else:
    print(f"{input_str} is not a binary string")