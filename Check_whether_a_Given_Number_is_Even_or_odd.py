# Given a number n, check whether a given number is even or odd.

# Return "even" if Even else "odd".

class Solution:
    def isEvenOrOdd(self, n: int) -> str:
        # Your code goes here
        if n%2==0:
            return 'even'
        else:
            return "odd"
