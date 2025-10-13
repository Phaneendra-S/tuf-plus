#You are given a string s. Your task is to calculate the frequency of each character in the string and return the result in a specific order.
#The result should consist of each distinct character followed by its frequency, sorted by character in ascending (lexicographical) order.

class Solution:
    def character_frequency(self, s: str) -> str:
        chars = set(s)
        l=[]
        for i in chars:
            count=s.count(i)
            l.append(i+str(count))
        return ' '.join(sorted(l))
