"""
You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array nums​​​, return the minimum number of elements to remove to make nums​​​ a mountain array.

 

Example 1:

Input: nums = [1,3,1]
Output: 0
Explanation: The array itself is a mountain array so we do not need to remove any elements.
Example 2:

Input: nums = [2,1,1,5,6,2,3,1]
Output: 3
Explanation: One solution is to remove the elements at indices 0, 1, and 5, making the array nums = [1,5,6,3,1].

nums = 
nums = 
nums = [100,92,89,77,74,66,64,66,64]
"""
from typing import List

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        
        # Step 1: Compute LIS from the left
        lis = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)   

        # Step 2: Compute LDS from the right
        lds = [1] * n
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[i] > nums[j]:
                    lds[i] = max(lds[i], lds[j] + 1)  
                                     
        # Step 3: Find maximum valid mountain array length
        max_mountain_len = 0
        for i in range(1, n-1):  # Peak cannot be at the edges
            if lis[i] > 1 and lds[i] > 1:
                max_mountain_len = max(max_mountain_len, lis[i] + lds[i] - 1)
    
        # Step 4: Calculate minimum removals
        return n - max_mountain_len

sol = Solution()
nums = [2,1,1,5,6,2,3,1]
print(sol.minimumMountainRemovals(nums))