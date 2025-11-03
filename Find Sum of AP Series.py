class Solution:
    def sumOfAP(self, n: int, a: int, d: int) -> int:
        # Your code goes here
        return int((n/2)*(2*a+(n-1)*d))
