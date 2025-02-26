"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""
from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        r_len = 0
        left = 0
        max_len = 0
        for i in range(n):
            if nums[i] & 1:
                r_len+=1
            else:
                r_len+=1
                k-=1

                if k < 0:
                    while nums[left] == 1:
                        r_len-=1
                        left+=1
                    r_len-=1
                    left+=1
                    k+=1

            if r_len > max_len:
                max_len = r_len
        return max_len
sol = Solution()
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
#nums = [1,1,1,0,0,0,1,1,1,1,0]
#k = 2
print(sol.longestOnes(nums,k))