"""
Given a list, write a function to get first, second best scores from the list.

List may contain duplicates.

Example

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
first_second(myList) # 90 87
"""

# def first_second(myList):
#     myList.sort(reverse=True)
#     print(myList[0])

# myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
# first_second(myList)

def remove_duplicates(arr):
    # TODO

    s = set(arr)
    print ([elem for elem in s])

remove_duplicates([1, 1, 2, 2, 3, 4, 5])