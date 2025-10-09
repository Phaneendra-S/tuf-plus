#Given an integer n, return true if and only if it is an Armstrong number.
#The k-digit number n is an Armstrong number if and only if the kth power of each digit sums to n.

class Solution:
    def isArmstrong(self, N: int) -> bool:
        k=len(str(N))
        digits=[]
        for i in str(N):
            digits.append(int(i))
        arm_sum=0
        for i in digits:
            arm_sum+=i**k

        return arm_sum==N
