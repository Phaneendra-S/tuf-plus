# Given an integer n, return true if it is an Abundant Number, otherwise return false.
# A number is called Abundant if the sum of its proper divisors (excluding the number itself) is greater than the number.

class Solution:
    def isAbundant(self, n: int) -> bool:
        # Your code goes here
        p=[]
        for i in range(1,(n//2)+1):
            if n%i==0:
                p.append(i)
        if sum(p)>n:
            return True
        else:
            return False
