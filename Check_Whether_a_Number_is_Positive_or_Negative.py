# Check Whether a Number is Positive or Negative

# Given an integer n, determine whether it is Positive, Negative, or Zero.

# Return the string:

# "Positive" if n > 0
# "Negative" if n < 0
# "Zero" if n == 0

class Solution:
    def checkNumberSign(self, n: int) -> str:
        # Your code goes here
        if n>0:
            return "Positive"
        elif n<0:
            return "Negative"
        else:
            return "Zero"
