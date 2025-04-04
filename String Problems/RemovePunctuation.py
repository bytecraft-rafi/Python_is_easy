#Write a Python Program to Remove Punctuation From a String
# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

print(type(punctuations))
my_str = input("Enter a string: ")
empty_string = ""
for char in my_str:
    if char not in punctuations:
        empty_string = empty_string + char

print(empty_string)
