"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
"""
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        def findRight(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
        
        left_index = findLeft(nums, target)
        right_index = findRight(nums, target)

        if left_index <= right_index and right_index < len(nums) and nums[left_index] == target and nums[right_index] == target:
            return [left_index, right_index]
        else:
            return [-1, -1]

        """
        start = -1
        end = -1
        i=0
        while i < len(nums) and end < len(nums):
            if nums[i] == target:
                start = i
                end = i
                while end+1 < len(nums) and nums[end+1] == target:
                    end+=1
                break
            i+=1
        return [start,end]       
        """

sol = Solution()
nums = nums = [5,7,7,8,8,10]
target = 8
print(sol.searchRange(nums,target))