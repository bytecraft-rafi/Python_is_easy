# Write a Python program to split words and join a string
inp_str = input("Enter your string : ")
word_list = inp_str.split()

# print(word_list)

# for word in word_list:
#     print(word)

seperator = " " # assigned space as the seperator
output = seperator.join(word_list)

print("Original String:", inp_str)
print("List of split Words:", word_list)
print("Joined String:", output)
