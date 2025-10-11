# Given two sorted arrays, nums1 and nums2, return an array containing the intersection of these two arrays. Each element in the result must appear as many times as it appears in both arrays.
# The intersection of two arrays is an array where all values are present in both arrays.

class Solution:
    def intersectionArray(self, nums1, nums2):
        set1=set(nums1)
        set2=set(nums2)
        result=[]
        for i in sorted(set1):
            if i in sorted(set2):
                count1=nums1.count(i)
                count2=nums2.count(i)
                for j in range(min(count1,count2)):
                    result.append(i)
        return result
