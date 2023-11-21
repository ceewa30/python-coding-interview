num = int(input("Enter the number for pattern: "))
# *****
#  *  *
#   * *
#    **
#     *

for i in range(num):
    for j in range(num):
        if i == 0 or j == (num-1) or j == i:
            print("*", end="")
        else:
            print(end=" ")
    print()