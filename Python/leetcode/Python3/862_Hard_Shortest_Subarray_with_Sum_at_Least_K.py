"""
Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [1], k = 1
Output: 1

Example 2:
Input: nums = [1,2], k = 4
Output: -1

Example 3:
Input: nums = [2,-1,2], k = 3
Output: 3
"""
from typing import List
from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        if nums[0] >= k:
            return 1

        # Need to calculate the prefix sums.
        prefixSums = []
        totalSum = nums[0]
        prefixSums.append(nums[0])
        for i in range(1, len(nums)):
            totalSum+=nums[i]
            prefixSums.append(totalSum)
        result = float('inf') 
        for i in range(len(prefixSums)):
            if prefixSums[i] >= k:
                result = min(result, i + 1)  # Use i + 1 because prefix sums are 0-indexed    

        queue = deque([0])
        for i in range(1, len(prefixSums)):
            while queue and prefixSums[i] - prefixSums[queue[0]] >= k:
                result = min(result, i - queue.popleft()) 
            while queue and prefixSums[i] <= prefixSums[queue[-1]]:
                queue.pop()
            queue.append(i)

        return result if result != float('inf') else -1


sol = Solution()
nums = [[1],[1,2],[2,-1,2],[-34,37,51,3,-12,-50,51,100,-47,99,34,14,-13,89,31,-14,-44,23,-38,6]]
k = [1, 4, 3, 151]

for i in range(len(nums)):
    print(sol.shortestSubarray(nums[i], k[i]))