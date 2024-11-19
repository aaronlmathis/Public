"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

"""
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = 0
        
        # Move all non-zero elements to the beginning of the list
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[x] = nums[i]
                x += 1
        
        for i in range(x, len(nums)):
            nums[i] = 0
            
        print(nums)
sol = Solution()
nums = [0,0,1]
print(sol.moveZeroes(nums))
