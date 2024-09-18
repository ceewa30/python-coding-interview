"""
Find the maximum product of two integers in an array where all elements are positive.

Example

arr = [1, 7, 3, 4, 9, 5]
"""

def max_product(arr):
    max1, max2 = 0, 0

    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

    return max1 * max2

arr = [1, 7, 3, 4, 9, 5]
prod = max_product(arr)
print(f"Product of  {arr[0]} and {arr[1]} is {prod}")