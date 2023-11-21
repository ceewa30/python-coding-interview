# step 1: Getting a number which is positive integer, but not less then 0
# step 2: if the number is greater than or equal to 0
# step 3: number = number plus function number minus 1
# step 4: print the number

# def sumofinteger(number):
#     result = 0
#     for val in number:
#         result += val
#     return result

def list_sum_recursive(number):
    if len(number) == 0:
        return 0
    return number[0] + list_sum_recursive(number[1::])
# def sumofinteger(number):
#     assert number >= 0 and int(number) ==  number, 'The number must be a positive integer!'
#     if number in [0,1]:
#         return 1
#     else:
#         return number + sumofinteger(number - 1)

number = [5, 2, 3, 4, 5]
print(list_sum_recursive(number))
