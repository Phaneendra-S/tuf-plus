# Given an array of n elements. The task is to return the count of the number of odd numbers in the array.

class Solution:
    def countOdd(self, arr, n):
        # Your code goes here
        count=0
        for i in arr:
            if i%2!=0:
                count+=1
        return count
