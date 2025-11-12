# You are given a floating-point number as input. Your task is to determine whether the number is even or odd.

# Unlike integers, you cannot determine evenness or oddness by simply looking at the last digit. You must consider only the integer part (i.e., the part before the decimal point) of the number and apply the standard rule:

# A number is even if its integer part is divisible by 2.
# A number is odd otherwise.

# Note:
# The digits after the decimal point are ignored.
# Trailing zeroes after the decimal point do not affect the result.

class Solution:
    def isEvenOrOdd(self, num: float) -> str:
        # Your code goes here
        if int(num)%2==0:
            return "even"
        else:
            return "odd"
