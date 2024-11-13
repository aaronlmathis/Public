"""
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

Example 1:
Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

Example 2:
Input: nums = [0,0,0,0,0], goal = 0
Output: 15
"""
from typing import List
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        #Count number of subarrs where curSum <= x
        def helper(x): 
            if x < 0: return 0

            res = 0
            l, cur = 0, 0
            for r in range(len(nums)):
                cur+=nums[r]
                while cur > x:
                    cur -= nums[l]
                    l+=1
                res+=(r-l+1)
            return res
        return helper(goal) - helper(goal - 1)
    
sol = Solution()
nums = [1,0,1,0,1]
goal = 2
print(sol.numSubarraysWithSum(nums, goal))