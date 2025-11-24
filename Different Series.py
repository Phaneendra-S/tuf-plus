# Return the nth term of the series given by:

# xi = i + xi-1 + 1, where n1 is the 1st term of the series and has value = 1.

class Solution:
    def nthSpecialElement(self, n):
        if n==1:
            return 1
        elif n>1:
            return n+self.nthSpecialElement(n-1)+1
