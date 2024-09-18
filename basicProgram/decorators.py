def my_decorators(func):
    '''Decorator function'''
    def wrapper():
        '''Return string F-I-B-O-N-A-C-C-I'''
        return 'F-I-B-O-N-A-C-C-I'
    return wrapper

@my_decorators
def pfib():
    '''Return Fibonacci'''
    return 'Fibonacci'

# pfid = my_decorators(pfib)
# print(pfib)
print(pfib())
