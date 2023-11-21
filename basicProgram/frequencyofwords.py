# Write a Python program to count the frequency of words appearing in a string

str = input("Enter a string: ")

def freq_words(str):
    freq = str.split()
    num_of_words = {}

    for i in freq:
        num_of_words[i] = num_of_words.get(i, 0) + 1
        # if i not in num_of_words.keys():
        #     num_of_words[i] = 0
        # num_of_words[i] = num_of_words[i] + 1
    return num_of_words

word_present = freq_words(str)
print(word_present)