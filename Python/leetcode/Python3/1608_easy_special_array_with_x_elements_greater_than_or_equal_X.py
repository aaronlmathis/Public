"""
You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.
Notice that x does not have to be an element in nums.
Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.
Example 1:
Input: nums = [3,5]
Output: 2
Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.

"""
from typing import List
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()  # Sort the array
        n = len(nums)
        
        for i in range(n):
            x = nums[i]
            count = n - i  # Number of elements >= nums[i]
            if count == x:
                return x
        
        # Check for the case where x could be greater than the maximum value in the array
        if nums[-1] < n:
            return n
        
        return -1
sol = Solution()
nums =  [3, 5]
print(sol.specialArray(nums))