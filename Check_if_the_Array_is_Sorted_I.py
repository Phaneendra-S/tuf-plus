#Given an array arr of size n, the task is to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order. If the array is sorted then return True, else return False.

class Solution:
    def arraySortedOrNot(self, arr, n):
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                return False
            else:
                continue
        return True
        
