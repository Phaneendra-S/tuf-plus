#my code
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_count=0
        count=0
        if len(nums)==1:
            if nums[0]==1:
                return 1
            else:
                return 0
        else:        
            for i in range(len(nums)):
                if nums[i]==1:
                    if i>0 and nums[i-1]==1:
                        count+=1
                    else:
                        count=1
                if count>=max_count:
                    max_count=count

        return max_count

#best code
class Solution:
def findMaxConsecutiveOnes(self, nums):
  max_count = 0
  count = 0
  for num in nums:
    if num == 1:
    count + = 1
  else:
    max_count = max(max_count, count)
    count = 0
    max_count = max(max_count, count)
  return max_count
