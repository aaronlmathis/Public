"""
An array is considered special if every pair of its adjacent elements contains two numbers with different parity.
You are given an array of integer nums and a 2D integer matrix queries, where for queries[i] = [fromi, toi] your task is to check that 
subarray nums[fromi..toi] is special or not.

Return an array of booleans answer such that answer[i] is true if nums[fromi..toi] is special.
 

Example 1:
Input: nums = [3,4,1,2,6], queries = [[0,4]]
Output: [false]
Explanation:
The subarray is [3,4,1,2,6]. 2 and 6 are both even.

Example 2:
Input: nums = [4,3,1,6], queries = [[0,2],[2,3]]
Output: [false,true]
Explanation:
The subarray is [4,3,1]. 3 and 1 are both odd. So the answer to this query is false.
The subarray is [1,6]. There is only one pair: (1,6) and it contains numbers with different parity. So the answer to this query is true.
"""
from typing import List
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        left = 0
        prefix = [0] * n
        for right in range(1, n):
            if nums[right] % 2 == nums[right-1] % 2:
                prefix[left] = right - 1

                for i in range(left+1, right):
                    prefix[i] = prefix[left]

                left = right
        prefix[left] = n - 1
        for i in range(left + 1, n):
            prefix[i] = prefix[left]

        ans = []
        for query in queries:
            if query[1] <= prefix[query[0]]:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans
                


     
nums = [4,3,1,6]
queries = [[0,2],[2,3]]
sol = Solution()
print(sol.isArraySpecial(nums, queries))