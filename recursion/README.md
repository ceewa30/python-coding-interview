# step 1: the number should be a positive integer and greater than 0
# step 2: if the number is greater then or equal to 0
# step 3: return 1
# step 4: number multiple by function number minus 1

# Python stores local variables on the stack of the interpreter, and so recursion takes up stack space of the interpreter.

# If the Python interpreter tries to go over the stack limit, the Linux kernel makes it segmentation fault.

# The stack limit size is controlled with the getrlimit and setrlimit system calls.

# Python offers access to those system calls through the resource module.

# Increase Recursion Limit
import sys
sys.setrecursionlimit(5000)