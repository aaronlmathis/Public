"""
Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.
A pair (i, j) is fair if:
    0 <= i < j < n, and
    lower <= nums[i] + nums[j] <= upper

    i < j which is < length of nums
    nums[i] + nums[j] greater than or equal to lower
    nums[i] + nums[j] less than or equal to upper.

Example 1:
Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).

Example 2:
Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).
"""
from typing import List
from bisect import bisect_left, bisect_right
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort() # sort nums in asc 
       
        n = len(nums)
        count = 0
        for left in range(n-1):
            rightMin = bisect_left(nums, lower - nums[left], left+1)

            rightMax = bisect_right(nums, upper - nums[left], left+1)

            count+= rightMax-rightMin
        
        return count
        nums.sort()
        ans = 0
        for i in range(len(nums) - 1):
            low = bisect_left(nums, lower - nums[i], i + 1)
            up = bisect_right(nums, upper - nums[i], i + 1)
            ans += up - low
        return ans
sol = Solution()
nums =[0,1,7,4,4,5]
lower = 3
upper = 6        
print(sol.countFairPairs(nums,lower,upper))