# Given an integer array nums sorted in non-decreasing order and an integer target, return true if target is a majority element, or false otherwise.
#A majority element in an array nums is an element that appears more than nums.length / 2 times in the array.

class Solution:
    def isMajorityElement(self, nums, target):
        # Your code goes here
        if target in nums:
            if nums.count(target)>len(nums)/2:
                return 1
        else:
            return 0
