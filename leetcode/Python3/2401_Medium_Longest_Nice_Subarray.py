"""
You are given an array nums consisting of positive integers.
We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.
Return the length of the longest nice subarray.
A subarray is a contiguous part of an array.
Note that subarrays of length 1 are always considered nice.

 

Example 1:
Input: nums = [1,3,8,48,10]
Output: 3
Explanation: The longest nice subarray is [3,8,48]. This subarray satisfies the conditions:
- 3 AND 8 = 0.
- 3 AND 48 = 0.
- 8 AND 48 = 0.
It can be proven that no longer nice subarray can be obtained, so we return 3.

Example 2:
Input: nums = [3,1,5,11,13]
Output: 1
Explanation: The length of the longest nice subarray is 1. Any subarray of length 1 can be chosen.

Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 109
"""
from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        curr_mask = 0 
        max_length = 0

        for right in range(len(nums)):
            # If the current number conflicts with the existing mask, shrink the window
            while (curr_mask & nums[right]) != 0:
                curr_mask ^= nums[left]  # Remove nums[left] from the bitmask
                left += 1  # Move left pointer forward

            # Add nums[right] to the current bitmask
            curr_mask |= nums[right]

            # Update max_length
            max_length = max(max_length, right - left + 1)

        return max_length


sol = Solution()
nums = [4, 8, 16, 32, 64, 128, 256, 512, 6]

#nums = [45106826,547958667,823366125,332020148,611677524,510346561,555831456,436600904,12594192,127206768,540754485,201997978,473116514,233000361,538246458,729745279,343417143,892046691,376031730]
#nums = [1,3,8,48,10]
#nums = [3,1,5,11,13]
#nums=[744437702,379056602,145555074,392756761,560864007,934981918,113312475,1090,16384,33,217313281,117883195,978927664]
nums=[84139415,693324769,614626365,497710833,615598711,264,65552,50331652,1,1048576,16384,544,270532608,151813349,221976871,678178917,845710321,751376227,331656525,739558112,267703680]
print(sol.longestNiceSubarray(nums))        