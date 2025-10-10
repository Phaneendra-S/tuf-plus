#You are given two fractions as strings in the form "a/b" and "c/d" where a, b, c, and d are positive integers and b ≠ 0, d ≠ 0.
#Your task is to add the two fractions and return their sum in the simplest form as a string "x/y".


class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def addFractions(self, frac1: str, frac2: str) -> str:
        frac1_parts = frac1.split('/')
        frac2_parts = frac2.split('/')

        frac1_num = int(frac1_parts[0])
        frac1_den = int(frac1_parts[1])
        frac2_num = int(frac2_parts[0])
        frac2_den = int(frac2_parts[1])

        if frac1_den == 0 or frac2_den == 0:
            return "Error: Denominator cannot be zero"

        sum_num = frac1_num * frac2_den + frac2_num * frac1_den
        sum_den = frac1_den * frac2_den

        if sum_den == 0:
            return "Error: Denominator cannot be zero"

        common_divisor = self.gcd(sum_num, sum_den)
        simplified_num = sum_num // common_divisor
        simplified_den = sum_den // common_divisor

        return f"{simplified_num}/{simplified_den}"
