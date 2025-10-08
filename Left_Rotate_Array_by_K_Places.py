class Solution:
    def rotateArray(self, nums, k: int) -> None:
        #method 1
        # for _ in range(k):
        #     i=nums[0]
        #     nums.remove(nums[0])
        #     nums.append(i)


        #method 2
        # Ensure k is within the range of array length
        k=k%len(nums)
        # Rotate the array using slicing and concatenation
        nums[:]=nums[k:]+nums[:k]
