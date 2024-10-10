# Linear Search Algorithm


def linear_search(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1



arr = [20,40,30,50,70]
value = 50
print(linear_search(arr, value))