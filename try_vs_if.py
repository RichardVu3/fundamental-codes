'''
These codes are used to test the time needed for if-clause and
error handling to run.
'''

import timeit

# Failed condition checking
setupfail = '''
a = 1
b = 0
'''

# Successful condition checking
setupsuccess = '''
a = 1
b = 1
'''

# Checked code for try and error handling
stmtif = '''
if b != 0:
    a/b
'''

stmttry = '''
try:
    a/b
except:
    pass
'''

# Main code to return time for comparison
t1 = timeit.timeit(setup = setupfail, stmt = stmtif)
t2 = timeit.timeit(setup = setupfail, stmt = stmttry)
t3 = timeit.timeit(setup = setupsuccess, stmt = stmtif)
t4 = timeit.timeit(setup = setupsuccess, stmt = stmttry)

print("Fail with if: {}".format(t1))
print("Fail with try: {}".format(t2))
print("Success with if: {}".format(t3))
print("Success with try: {}".format(t4))