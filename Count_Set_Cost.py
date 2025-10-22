#Given two integers n and k, return the cost offlipping all set bits in n. One flip operation costs k.

# class Solution:
#     def setBitCost(self, n, k):
#         # set_bits=[]
#         count=0
#         while n!=1:
#             r=n%2
#             if r==1:
#                 # set_bits.append(r)
#                 count+=1
#             n//=2
#         # if n==1:
#         #     set_bits.append(n)
#         # return len(set_bits)*k
#         return (count+1)*k

class Solution:
    def setBitCost(self, n, k):
        count = 0
        while n > 0:           # Loop continues as long as n is positive
            count += n & 1      # Add 1 if the rightmost bit is set
            n //=2             # Right shift n by 1 (equivalent to n //= 2)
        return count * k        # No need for +1; this counts all set bits

