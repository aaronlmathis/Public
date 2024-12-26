"""
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1
"""
from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = 0
        for num in nums:
            total_sum += num
        if abs(target) > total_sum or (target+total_sum) % 2 != 0:
            return 0
        
        sum = (total_sum + target) // 2
        dp = [0] * (sum+1)

        dp[0] = 1

        for num in nums:
            for j in range(sum, num-1, -1):
                dp[j] += dp[j-num]

        return dp[sum]
    
sol = Solution()
nums = [1,1,1,1,1]
target = 3
print(sol.findTargetSumWays(nums, target))