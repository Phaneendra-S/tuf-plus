#You are given a binary number N (represented as a string or integer). Your task is to convert it into its corresponding decimal (base-10) number.

class Solution:
    def binaryToDecimal(self, N):
        # Your code goes here
        res=0
        for i,j in enumerate(str(N)):
            res+=(int(j))*(2**(len(str(N))-i-1))
        return res
