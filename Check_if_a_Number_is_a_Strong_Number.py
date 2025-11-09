# Given a positive integer N, determine whether it is a Strong Number or not.

# A number is considered a Strong Number if the sum of the factorial of its digits is equal to the number itself.

# Return "Yes" if the number is a Strong Number, else return "No".

import math
class Solution:
    def isStrongNumber(self, n):
        # Your code goes here
        s=str(n)
        sum=0
        for i in s:
            sum+=math.factorial(int(i))
        if sum==n:
            return "Yes"
        else:
            return "No"
