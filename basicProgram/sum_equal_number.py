# Write a program to find all pairs of integers whose sum is equal to a given number.

# [2,6,3,9,11]    9   -----> [6, 3 ]

"""
Exampl:
Input : nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Output: Because nums[0] + num[1] == 9, we return [0,1]

- Does array contain only positive or negative numbers?
- What if the same pair repeats twice, should we print it every time ?
- If the reverse of the pair is acceptable e.g. Can we print both (4,1) and (1,4) if the given sum is 5.
- Do we need to print only distinct pairs? does (3, 3) is valid pair forgiven sum of 6 ?
- How big is the array ?
"""

def findPairs(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            # if its distinct pairs
            if nums[i] == 0 or nums[i] == nums[j]:
                 continue 
            if nums[i] + nums[j] == target:
                   print(i, j) 

arr = [1, 2, 3, 2, 3, 4, 5, 6]
findPairs(arr, 6)


