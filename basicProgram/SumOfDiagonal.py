"""
Given 2D list calculate the sum of diagonal elements.

Example

myList2D= [[1,2,3],
           [4,5,6],
           [7,8,9]] 
 
diagonal_sum(myList2D) # 15
"""

def SumOfDiagonal(arr):
    total = 0
    for i in range(len(arr)):
        print(arr[i][i])
        total += arr[i][i]
    print(total)        

myList2D= [[1,2,3],
           [4,5,6],
           [7,8,9]] 

SumOfDiagonal(myList2D)