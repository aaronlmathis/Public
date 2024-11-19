"""
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
Return the number of nice sub-arrays.

Example 1:
Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:
Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.

Example 3:
Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
"""
from typing import List
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [0 if x % 2 == 0 else 1 for x in nums]

        def count(x): 
            if x < 0: return 0

            res = 0
            l, cur = 0, 0
            for r in range(len(nums)):
                cur+=nums[r]
                while cur > x:
                    cur -= nums[l]
                    l+=1
                res+=(r-l+1)
            return res
        
        return count(k) - count(k - 1)

sol = Solution()
nums = [1,1,2,1,1]
k = 3
print(sol.numberOfSubarrays(nums, k))