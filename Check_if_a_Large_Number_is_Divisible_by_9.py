# You are given a string s representing a large non-negative integer. Your task is to determine whether this number is divisible by 9 or not.
# Due to the large size of the number, you cannot store it in standard numeric data types like int, long, or long long. You must process it as a string.
# A number is divisible by 9 if and only if the sum of its digits is divisible by 9.

class Solution:
    def isDivisibleBy9(self, s: str) -> bool:
        # Your code goes here
        sum=0
        for i in s:
            sum+=int(i)
        if sum%9==0:
            return True
        else:
            return False
