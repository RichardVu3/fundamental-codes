"""
Calculate Greatest Common Divisor of 2 integers.
"""

a = int(input("a = "))
b = int(input("b = "))

if a < b:
    c = a
else:
    c = b

def gcd(a, b, c):
    print("Greatest Common Divisor of {} and {} is {}".format(a, b, c))

def gcdRecur1(a, b, c):
    if a%c == 0 and b%c == 0:
        return gcd(a, b, c)
    else:
        return gcdRecur1(a, b, c-1)
 
gcdRecur1(a, b, c)

#Euclid's algorithm to find out the GCD:
def gcdRecur(a,b):
    if b==0:
        return a
    elif a==0:
        return b
    else:
        return gcdRecur(b,a%b)

c = gcdRecur(a, b)

print("Greatest Common Divisor of {} and {} (Euclid's algorithm) is {}".format(a, b, c))