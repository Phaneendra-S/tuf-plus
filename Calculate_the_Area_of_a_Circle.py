#Given an integer r representing the radius of a circle, return the area of the circle, calculated using the formula:
#Area = π × r²
#Use the value of π as 3.14 and return the result rounded to 1 decimal place.


class Solution:
    def areaOfCircle(self, r):
        # Your code goes here
        a=3.14*r*r
        return round(a,1)
