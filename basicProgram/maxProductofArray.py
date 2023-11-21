"""
Find the maximum product of two integers in an array where all elements are positive.

Example

arr = [1, 7, 3, 4, 9, 5] 
"""

def max_product(arr):
    arr.sort(reverse=True)
    return arr[0]*arr[1]

arr = [1, 7, 3, 4, 9, 5] 
prod = max_product(arr)
print(f"Product of  {arr[0]} and {arr[1]} is {prod}")