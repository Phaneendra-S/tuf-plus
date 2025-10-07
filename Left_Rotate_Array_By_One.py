#Given an integer array nums, rotate the array to the left by one.
#Note: There is no need to return anything, just modify the given array.

class Solution:
    def rotateArrayByOne(self, nums):
        i=nums[0]
        nums.remove(nums[0])
        nums.append(i) 
