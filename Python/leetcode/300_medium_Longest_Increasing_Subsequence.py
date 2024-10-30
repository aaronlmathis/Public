"""
Given an integer array nums, return the length of the longest strictly increasing 
subsequence
.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
"""
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
  
        sub = [nums[0]]
        def binary_search(val):
            left, right = 0, len(sub)-1
            while left <= right:
                mid = (left + right) // 2
                if sub[mid] < val:
                    left = mid + 1
                else: 
                    right = mid - 1
            
            return left
        

        for i in range(1, len(nums)):
            if nums[i] > sub[-1]:
                sub.append(nums[i])
            else:
                pos = binary_search(nums[i])
                sub[pos] = nums[i]

        return len(sub)



sol=Solution()
nums = [10,9,2,5,3,7,101,18]
print(sol.lengthOfLIS(nums))