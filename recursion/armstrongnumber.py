def armstrongnumber(n):
    """Return the sum of digit of positive integer n."""
    if n < 10:
        return n
    else:
       all_but_last = n // 10
       last = n % 10
       return armstrongnumber(all_but_last) + last

print(armstrongnumber(25))
