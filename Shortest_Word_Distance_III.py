#Given an array of strings wordsDict and two strings that already exist in the array word1 and word2, return the shortest distance between the occurrence of these two words in the list.
# Note that word1 and word2 may be the same. It is guaranteed that they represent two individual words in the list.


class Solution(object):
    def shortestWordDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # Your code goes here
        word1_index=[]
        word2_index=[]
        for i,j in enumerate(wordsDict):
            if j==word1:
                word1_index.append(i)
            elif j==word2:
                word2_index.append(i)
        if word1==word2:
            if len(word1_index) < 2:
                return 0 # or some error, not enough occurrences
            min_dist = len(wordsDict)
            for i in range(1, len(word1_index)):
                min_dist = min(min_dist, word1_index[i] - word1_index[i-1])
            return min_dist
        else:
            min_dist = len(wordsDict)
            for i in word1_index:
                for j in word2_index:
                    min_dist = min(min_dist, abs(i - j))
            return min_dist





        
