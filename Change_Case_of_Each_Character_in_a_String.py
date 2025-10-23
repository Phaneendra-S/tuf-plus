#Given a string s, write a program to invert the case of each character:
# Convert lowercase letters to uppercase
# Convert uppercase letters to lowercase
# Leave non-alphabetic characters unchanged

class Solution:
    def toggle_case(self, s: str) -> str:
        # Your code goes here
        letters=[]
        for i in s:
            letters.append(i)
        for i in range(len(s)):
            if s[i].islower():
                letters[i]=s[i].upper()
            elif s[i].isupper():
                letters[i]=s[i].lower()
        return ''.join(letters)
