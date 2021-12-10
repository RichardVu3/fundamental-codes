"""
The function is to determine if a string is a Palindrome.
"""

def isPal(s):
    def tochar(s):
        s = s.lower()
        string = ''
        for char in s:
            if char in 'abcdefghijklmnopqrstuvwxyz':
                string = string + char
        return string
    
    def checkPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and checkPal(s[1:-1])
    
    return checkPal(tochar(s))

print(isPal("Was it a car or a cat I saw"))
