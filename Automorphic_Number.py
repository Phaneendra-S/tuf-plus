# Given a positive integer N, determine whether it is an Automorphic Number.
#A number is called an Automorphic Number if the square of the number ends with the number itself.

class Solution:
    def isAutomorphic(self, n: int) -> bool:
        sq = n*n
        n_length = len(str(n))
        sq_length = len(str(sq))

        if str(sq)[-n_length:]==str(n):
            return True
        else:
            return False
