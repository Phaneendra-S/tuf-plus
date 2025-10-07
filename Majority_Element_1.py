# question:

# Given an integer array nums of size n, return the majority element of the array.
# The majority element of an array is an element that appears more than n/2 times in the array. The array is guaranteed to have a majority element.

# answer:

class Solution:
    def majorityElement(self, nums):
        set_nums=set(nums)
        for i in set_nums:
            count=0
            for j in nums:
                if i==j:
                    count+=1
            if count>len(nums)/2:
                return i
