"""
Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. 
It is not allowed to remove the whole array.
Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.
A subarray is defined as a contiguous block of elements in the array.

Example 1:
Input: nums = [3,1,4,2], p = 6
Output: 1
Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.

Example 2:
Input: nums = [6,3,5,2], p = 9
Output: 2
Explanation: We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.

Example 3:
Input: nums = [1,2,3], p = 3
Output: 0
Explanation: Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.
"""
from typing import List
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        # Calculate the total sum of the array
        total_sum = sum(nums)
        target_remainder = total_sum % p
        
        # If total_sum is already divisible by p, return 0
        if target_remainder == 0:
            return 0

        # Dictionary to store the latest index for a given remainder
        remainder_map = {0: -1}
        prefix_sum = 0
        min_length = len(nums)
        
        for i, num in enumerate(nums):
            prefix_sum += num
            current_remainder = prefix_sum % p
            
            # We need a prefix whose remainder would make current_remainder = target_remainder
            # target_remainder + x ≡ current_remainder (mod p), or x ≡ current_remainder - target_remainder (mod p)
            desired_remainder = (current_remainder - target_remainder) % p
            
            if desired_remainder in remainder_map:
                min_length = min(min_length, i - remainder_map[desired_remainder])
            
            # Update the remainder map
            remainder_map[current_remainder % p] = i
        
        # If we didn't find any valid subarray, return -1
        return min_length if min_length < len(nums) else -1
        

sol = Solution()
nums = [6,3,5,2]
p = 9

print(sol.minSubarray(nums, p))
        