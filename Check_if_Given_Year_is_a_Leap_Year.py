# Given an integer year, determine whether it is a leap year. Return "Yes" if it is a leap year, otherwise return "No".

class Solution:
    def isLeapYear(self, year: int) -> str:
        # Your code goes here
        if (year%100==0) and (year%400==0):
            return "Yes"
        elif (year%4==0) and (year%100!=0):
            return "Yes"
        else:
            return "No"
