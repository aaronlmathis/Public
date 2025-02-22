"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""
from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        left, zero_count, max_sum = 0,0,0

        for right in range(n):
            if nums[right] == 0:
                zero_count+=1
            
            while zero_count > 1:
                if nums[left]==0:
                    zero_count-=1
                left+=1
            
            if right-left > max_sum:
                max_sum = right-left
        return max_sum
    
    """
        n = len(nums)
        if n == 1: return 0  # If only one element, must delete it
        
        dp = [[0] * 2 for _ in range(n)]  # dp[i][0] = no delete, dp[i][1] = deleted one
        
        dp[0][0] = nums[0]
        dp[0][1] = 0  # No zero removed yet

        max_len = 0

        for i in range(1, n):
            if nums[i] == 1:
                dp[i][0] = dp[i-1][0] + 1
                dp[i][1] = dp[i-1][1] + 1
            else:
                dp[i][0] = 0
                dp[i][1] = dp[i-1][0]  # Best length if removing this zero
                
            max_len = max(max_len, dp[i][1])

        return max_len
    """

sol = Solution()
nums = [0,1,1,1,0,1,1,0,1]        
print(sol.longestSubarray(nums))