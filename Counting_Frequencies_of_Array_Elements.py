#Given an array nums of size n which may contain duplicate elements, return a list of pairs where each pair contains a unique element from the array and its frequency in the array.
#You may return the result in any order, but each element must appear exactly once in the output.

class Solution:
    def countFrequencies(self, nums):
        # Your code goes here
        unique_nums=set(nums)
        output=[]
        for i in unique_nums:
            freq=[]
            count=0
            for j in nums:
                if i==j:
                    count+=1
                    # nums.remove(j)
            freq.append(i)
            freq.append(count)
            if True:
                output.append(freq)
        return output

