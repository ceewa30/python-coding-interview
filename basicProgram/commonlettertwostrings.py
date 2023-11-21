# Write a Python program to find out common letters between two strings
# Example: common, two strings

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

def commonletters(str1, str2):
    s1 = set(str1)
    s2 = set(str2)
    common = s1 & s2
    return common

common_string = commonletters(str1, str2)
print(common_string)

