# Write a Python Program to Sort Words in Alphabetic Order
my_str = input("Enter a string: ")

words = [word.capitalize() for word in my_str.split()]  # breakdown the string into a list of words
words.sort()

print("The sorted words are:")
for word in words:
    print(word)
