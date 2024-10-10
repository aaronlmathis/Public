"""
A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.
Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

Example 1:
Input: nums = [6,0,8,2,1,5]
Output: 4
Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.

Example 2:
Input: nums = [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.
 

from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_amount = 0
        for i in range(len(nums) -1):
            for j in range(i+1, len(nums)):
                if nums[i] <= nums[j]:
                    distance = abs(j - i)
                    if distance > max_amount:
                        max_amount = distance

        return max_amount
"""
from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_right = [0] * len(nums)
        i = len(nums) - 1
        prev_max= 0
        for n in reversed(nums):
            max_right[i] = max(n, prev_max)
            prev_max = max_right[i]
            i-=1
        
        res = 0
        l = 0
        for r in range(len(nums)):
            while nums[l] > max_right[r]:
                l += 1
            res = max(res, r - l)
        return res
sol = Solution()
nums = [6,0,8,2,1,5]
print(sol.maxWidthRamp(nums))        