'''
Test some Fibonacci functions.
These functions use recursion to return the nth element of the sequence and 
keep track of the efficiency by the number of recursion.
'''

# fib1: basic recursion
def fib1(n):
    global recur_call
    recur_call += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib1(n-1) + fib1(n-2)

# fib2: memoization with dictionary
def fib2(n,fib_dict):
    global recur_call
    recur_call += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n in fib_dict:
        return fib_dict[n]
    else:
        fib_dict[n] = fib2(n-1,fib_dict) + fib2(n-2,fib_dict)
        return fib_dict[n]
    
# fib3: instead of checking n in fib2, check n-1 and n-2
def fib3(n,fib_dict):
    global recur_call
    recur_call += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    if n-1 not in fib_dict:
        fib_dict[n-1] = fib3(n-1,fib_dict)
    if n-2 not in fib_dict:
        fib_dict[n-2] = fib3(n-2,fib_dict)
    fib_dict[n] = fib_dict[n-1] + fib_dict[n-2]
    return fib_dict[n]

# fib4: instead of using if in fib3, use error handling
def fib4(n,fib_dict):
    global recur_call
    recur_call += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    try:
        fib_dict[n-1]
    except:
        fib_dict[n-1] = fib4(n-1,fib_dict)
    try:
        fib_dict[n-2]
    except:
        fib_dict[n-2] = fib4(n-2,fib_dict)
    fib_dict[n] = fib_dict[n-1] + fib_dict[n-2]
    return fib_dict[n]


# Main code to run those Fibonacci functions
n = 20
# Run fib1
recur_call = 0
print("fib1 result: {}".format(fib1(n)))
print("fib1 recursion calls: {}".format(recur_call))
print()

# Run fib2
recur_call = 0
fib_dict = {}
print("fib2 result: {}".format(fib2(n,fib_dict)))
print("fib2 recursion calls: {}".format(recur_call))
print(fib_dict)
print()

# Run fib3
recur_call = 0
fib_dict = {}
print("fib3 result: {}".format(fib3(n,fib_dict)))
print("fib3 recursion calls: {}".format(recur_call))
print(fib_dict)
print()

# Run fib4
recur_call = 0
fib_dict = {}
print("fib4 result: {}".format(fib4(n,fib_dict)))
print("fib4 recursion calls: {}".format(recur_call))
print(fib_dict)
print()