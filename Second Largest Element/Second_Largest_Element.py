#Given an array of integers nums, return the second-largest element in the array. If the second-largest element does not exist, return -1.

class Solution:
    def secondLargestElement(self, nums):
        set_nums=set(nums)
        nums_list=list(set_nums)
        nums_list.sort(reverse=True)
        if len(nums_list)>=2:
            if nums_list[0]==nums_list[1]:
                return -1
            else:
                return nums_list[1]
        else:
            return -1
