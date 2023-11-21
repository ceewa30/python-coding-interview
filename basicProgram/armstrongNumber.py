# for i in range(100, 1001):
#     num = i
#     result = 0
#     n = len(str(i))
#     while( i != 0):
#         digit = i % 10
#         result = result + digit ** n
#         i = i // 10
#     if num == result:
#         print(num)


number = int(input("Enter the three digit number to Armstrong Number or not :"))
numb = number
result = 0
n = len(str(numb))
for i in range(n):
    digit = number % 10
    result = result + digit ** n
    number = number // 10
    
if numb == result:
    print("The number is Armstrong Number")
else:
    print("The number is not an Armstrong Number")
