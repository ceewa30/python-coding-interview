# Missing Number

# 1+2+3+ ... +n = n(n+1)/2

def findmissing(arrnum, n):
    # Calculate the sum of first n natural numbers
    totalNumber = n*(n+1)/2
    print(totalNumber)

    # Calculate the sum of numbers in the array
    sumofarray = sum(arrnum)

    # Find the missing number by subtracting sum_arr from total
    missing = int(totalNumber - sumofarray)

    return missing

print(findmissing([1,2,3,4,6], 6))
