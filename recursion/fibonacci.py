
def fibonacci_iterative(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def fibonacci(number):
    """Return the nth number in the Finonacci sequence"""
    assert number >= 0 and int(number) == number, 'Fibonacci must be a integer number!'
    if number in [0,1]:
        return number
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

print(fibonacci(10))


