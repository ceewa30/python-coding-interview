# Write a program to find all pairs of integers whose sum is equal to a given number.

# [2,6,3,9,11]    9   -----> [6, 3 ]

def two_sum(nums, target):
    nums_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in nums_dict:
            return [nums_dict[complement], i]
        nums_dict[num] = 1


nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))

# Note: The above solution has a time complexity of O(n), where n is the length of the input array.

"""
def two_sum(nums, target): Define a function called two_sum that takes a list of integers nums and an integer target as input.

nums_dict = {} Create an empty dictionary nums_dict to store the numbers you have seen so far and their indices. Dictionary operations (adding and searching) have an average-case time complexity of O(1).

for i, num in enumerate(nums): Iterate through the input list nums using the enumerate function, which returns both the index i and the value num for each element in the list. The loop runs n times, where n is the length of the input list nums.

complement = target - num Calculate the complement of the current number num with respect to the target.

if complement in nums_dict: Check if the complement is present in the nums_dict dictionary. This operation has an average-case time complexity of O(1).

return [nums_dict[complement], i] If the complement is found in the nums_dict dictionary, return the index of the complement (nums_dict[complement]) and the current index i.

nums_dict[num] = i If the complement is not found, add the current number num and its index i to the nums_dict dictionary. This operation has an average-case time complexity of O(1).
"""
