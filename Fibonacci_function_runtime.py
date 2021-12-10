"""
These codes are used to measure the runtime of different Fibonacci functions
(from Fibonacci_verse.py)

# Remember to comment out the variable 'recur_call' in each function in
  Fibonacci_verse.py before running these codes.
"""

import timeit

# setup codes
setupfib = '''
import Fibonacci_verse
n = 100
fib_dict = {}
'''

stmtfib1 = '''
print("fib1 result: {}".format(Fibonacci_verse.fib1(n)))
'''

stmtfib2 = '''
print("fib2 result: {}".format(Fibonacci_verse.fib2(n,fib_dict)))
'''

stmtfib3 = '''
print("fib3 result: {}".format(Fibonacci_verse.fib3(n,fib_dict)))
'''

stmtfib4 = '''
print("fib4 result: {}".format(Fibonacci_verse.fib4(n,fib_dict)))
'''

# Runtime
'''
t1 = timeit.timeit(setup = setupfib, stmt = stmtfib1, number = 1)
print(t1)
print()
'''

t2 = timeit.timeit(setup = setupfib, stmt = stmtfib2, number = 1)
print(t2)
print()

t3 = timeit.timeit(setup = setupfib, stmt = stmtfib3, number = 1)
print(t3)
print()

t4 = timeit.timeit(setup = setupfib, stmt = stmtfib4, number = 1)
print(t4)
print()