# Given a positive integer N, determine whether it is a Harshad number (also known as a Niven number) or not.
# A number is said to be a Harshad number if it is divisible by the sum of its digits.

class Solution:
    def isHarshad(self, n: int) -> bool:
        # Your code goes here
        N=str(n)
        sum=0
        for i in N:
            sum+=int(i)
        if n%sum==0:
            return True
        else:
            return False
