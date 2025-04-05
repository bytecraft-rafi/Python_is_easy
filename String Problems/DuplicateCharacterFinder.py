#Write a Python program to find all duplicate characters in string

def duplicates(input_str):
    char_count = {} #dictionary to store every char count
    duplicates = [] #List to store duplicates

    for i in input_str:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1


    for i, count in char_count.items():
         if count > 1:
                 duplicates.append(i)

    return duplicates


# Input a string
input_string = "Abdullah Al Rafi"
# Find duplicate characters in the string
duplicate_chars = duplicates(input_string)
# Print the list of duplicate characters
print("Duplicate characters:", duplicate_chars)
    
