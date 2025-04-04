#Write a Python program to find uncommon words from two Strings.
def uncommon_words(string1, string2):
    word1 = set(string1.split())
    word2 = set(string2.split())


    uncommon_words_list = list(word1.symmetric_difference(word2))
    return uncommon_words_list


A= "I am not the only one"
B= "I am the only one in this mess"

print("Uncommon words: ", uncommon_words(A, B) )

