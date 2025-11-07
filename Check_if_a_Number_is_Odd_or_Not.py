# Given a non-negative integer n, determine whether it is odd.

# Return true if the number is odd, otherwise return false.

# A number is odd if it is not divisible by 2 (i.e., n % 2 != 0).

class Solution:
    def isOdd(self, n: int) -> bool:
        # Your code goes here
        if n%2==0:
            return False
        else:
            return True
