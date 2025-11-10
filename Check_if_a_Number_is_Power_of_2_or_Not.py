# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two if there exists an integer x such that n == 2x.
# You must solve it without using loops or recursion.

import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n>=1:
            value=math.log(n,2)
            
        if n<1:
            return False
        elif 0<value-int(value)<1:
            return False
        else:
            return True
