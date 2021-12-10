"""
This function is to find the longest substring in alphabetical order inside
a random string of characters.
"""
# i.e with s = 'azcbobobegghakl', expected output is 'beggh'

s = input("Input a string with random character: ")
count = 0
for char in range(len(s)):
    if char == len(s)-1:
        break
    else:
        string = s[char]
        while s[char] <= s[char+1]:
            string = string + s[char+1]
            char += 1
            if char == len(s)-1:
                break
        length = len(string)
        if length > count:
            count = length
            result = string
print(result)
    
