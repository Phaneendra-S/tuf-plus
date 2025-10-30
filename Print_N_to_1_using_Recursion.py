#Given an integer n, write a function to print all numbers from n to 1 (inclusive) using recursion.
# You must not use any loops such as for, while, or do-while.
# The function should print each number on a separate line, in decreasing order from n to 1

class Solution:
    def printNumbers(self, n):
        # Your code goes here
        print(n)
        if n-1>0:
            self.printNumbers(n-1)
