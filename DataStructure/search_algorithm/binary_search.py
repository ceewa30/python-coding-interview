# Binary search algorithm


import math
def binary_search(arr, value):
    start = 0
    end = len(arr) - 1
    mid = math.floor((start + end) / 2)
    while not arr[mid] == value and start <= end:
        if value < arr[mid]:
            end = mid -1
        else:
            start = mid + 1
            mid = math.floor((start + end) / 2)
        if arr[mid] == value:
            return mid
        else:
            return -1


arr = [2, 3, 4, 10, 40]
value = 10
print(binary_search(arr, value))