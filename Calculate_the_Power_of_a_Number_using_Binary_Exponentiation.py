#You are given two integers x and n. Your task is to calculate xn using Binary Exponentiation, and return the result modulo 10⁹ + 7.

class Solution:
    def power(self, x: int, n: int) -> int:
        # Your code goes here
        MOD = 10**9 + 7
        res = 1
        while n > 0:
            if n % 2 == 1:
                res = (res * x) % MOD
            x = (x * x) % MOD
            n = n // 2
        return res
