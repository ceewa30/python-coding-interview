# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# num = int(input("Enter the number for pattern: "))

# for i in range(1, num+1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

# num = int(input("Enter the number for pattern: "))

# for i in range(1, num+1):
#     for j in range(1, i+1):
#         print(i, end=" ")
#     print()

# *    
# **   
# * *  
# *  * 
# *****
num = int(input("Enter the number for pattern: "))

for i in range(num):
    for j in range(num):
        if j == 0 or i == (num-1) or j == i:
            print("*", end="")
        else:
            print(end=" ")
    print()

