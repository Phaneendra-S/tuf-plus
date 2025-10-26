#A dieter tracks their calorie intake over several days, represented as an array calories[i].

# Given an integer k, for each consecutive sequence of k days (calories[i], calories[i+1], ..., calories[i+k-1] for all 0 <= i <= n-k), they calculate T, the total calories consumed in that sequence:

# If T < lower, they performed poorly and lose 1 point.
# If T > upper, they performed well and gain 1 point.
# Otherwise, they performed normally, and no points are gained or lost.

# Initially, the dieter has zero points. Return the total number of points the dieter has after calories.length days.

# The total points can be negative.

class Solution:
    def dietPlanPerformance(self, calories, k, lower, upper):
        # Your code goes here
        n=len(calories)
        points=0
        total=0
        for i in range(k):
            total+=calories[i]
        if total<lower:
            points-=1
        elif total>upper:
            points+=1
        for i in range(1,n-k+1):
            # cal=0
            # for j in range(k):
                # cal+=calories[i+j]
            total+=calories[i+k-1]-calories[i-1]
            if total<lower:
                points-=1
            elif total>upper:
                points+=1
        return points

