#You are given an integer n. You need to check whether the number is a palindrome number or not. Return true if it's a palindrome number, otherwise return false.
# A palindrome number is a number which reads the same both left to right and right to left.

class Solution:
    def isPalindrome(self, n):
        strn=str(n)
        for i in range((len(strn)//2)):
            if strn[i]==strn[len(strn)-i-1]:
                continue
            else:
                return False
        return True
