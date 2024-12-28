"""
Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

 

Example 1:

Input: nums = [1,2,1,2,6,7,5,1], k = 2
Output: [0,3,5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
Example 2:

Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
Output: [0,2,4]
 
"""
from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        sums = [sum(nums[i:i+k]) for i in range(n-k+1)]
        ns = len(sums)

        best_left = 0
        left = [0] * ns
        for i in range(1, ns):   
            if sums[i] > sums[best_left]:
                best_left = i
            left[i] = best_left
        
        best_right = ns - 1
        right = [0] * ns
        right[best_right] = best_right
        for i in range(best_right-1, -1, -1):
            if sums[i] >= sums[best_right]:
                best_right= i
            right[i] = best_right
            print(i)
        print(f"sums: {sums}")
        print(f"Left: {left} - Best: {best_left}")
        print(f"Right: {right} - Best: {best_right}")
        result = []
        max_sum = -1
        for m in range(k, ns-k):
            l = left[m-k]
            r = right[m+k]
            s = sums[l] + sums[m] + sums[r]
            if s > max_sum:
                max_sum = s
                result = [l, m, r]

        return result

sol = Solution()
nums = [[1,2,1,2,6,7,5,1],[1,2,1,2,1,2,1,2,1],[7,13,20,19,19,2,10,1,1,19]]
k = [2,2,3]
for i in range(len(nums)):
    print(f"Example: {i+1}: {sol.maxSumOfThreeSubarrays(nums[i], k[i])}")       