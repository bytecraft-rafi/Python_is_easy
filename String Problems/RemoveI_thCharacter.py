# Write a Python program for removing ith character from a string

def remove_char(input_str, i):
    if i < 0 or i > len(input_str):
        print("Invalid Index!")
        print("Given string remains unchanged")
        result_str = input_str
        return result_str

    else:
        result_str = input_str[:i] + input_str[i+1:]
        return result_str


input_str = "Python is not easy!"
i = int(input("Enter the index of the char you want to remove: "))

# Remove the i-th character
new_str = remove_char(input_str, i)
print(f"Original String: {input_str}")
print(f"String after removing {i}th character : {new_str}")