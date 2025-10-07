# Given an array of integers nums, return the value of the largest element in the array

class Solution:
    def largestElement(self, nums):
        nums.sort()
        return nums[len(nums)-1]
