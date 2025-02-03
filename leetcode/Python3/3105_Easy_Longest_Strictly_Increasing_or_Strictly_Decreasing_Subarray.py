"""
You are given an array of integers nums. Return the length of the longest subarray of nums which is either strictly increasing or strictly decreasing.

Example 1:
Input: nums = [1,4,3,3,2]
Output: 2
Explanation:
The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].
The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].
Hence, we return 2.

Example 2:
Input: nums = [3,3,3,3]
Output: 1
Explanation:
The strictly increasing subarrays of nums are [3], [3], [3], and [3].
The strictly decreasing subarrays of nums are [3], [3], [3], and [3].
Hence, we return 1.

Example 3:
Input: nums = [3,2,1]
Output: 3
Explanation:
The strictly increasing subarrays of nums are [3], [2], and [1].
The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].
Hence, we return 3.

Constraints:
1 <= nums.length <= 50
1 <= nums[i] <= 50
"""
from typing import List
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # Let n be length of nums array
        n = len(nums)
        # Quick Exits:
        if n == 0:
            return 0
        # initialize variables to track increasing length, decreasing length, and max length
        ilen = dlen = mlen = 1 

        # Iterate through nums starting at 1. Each iteration, compare the number to its previous number
        # If it is greater than, increase ilen, set dlen to 1. 
        # If it is less than, increase dlen, set ilen to 1.
        # If it is neither, set both ilen and dlen to 1.
        # Calculate the max length seen `mlen` by using max()
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                ilen += 1
                dlen = 1
            elif nums[i] < nums[i-1]:
                dlen+=1
                ilen=1
            else:
                ilen =1
                dlen = 1
            
            mlen = max(mlen, ilen, dlen)

        return mlen
    
sol = Solution()
nums = [3,2,1]
print(sol.longestMonotonicSubarray(nums))        