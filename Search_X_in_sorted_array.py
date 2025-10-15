class Solution:
    def search(self, nums, target):
        return self.binarysearch(nums, 0, len(nums) - 1, target)

    def binarysearch(self, nums, start, end, target):
        if start > end:
            return -1

        mid = (start + end) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binarysearch(nums, start=mid + 1, end=end, target=target)
        else:
            return self.binarysearch(nums, start=start, end=mid - 1, target=target)
