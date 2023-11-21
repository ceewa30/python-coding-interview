# Write a Python program to convert two lists into a dictionary

def list_to_dict():
    list1 = [1, 2, 3]
    list2 = ["one", "two", "three"]
    result = dict(zip(list1, list2))
    return result

print(list_to_dict())

def dict_to_tuple():
    x={1: 'one', 2: 'two', 3: 'three'}
    for i in x.items():
        print(i)

dict_to_tuple()
    