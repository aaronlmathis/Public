"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 
"""
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert nums list into set
        nums = set(nums)

        longest_count = 0

        for num in nums:
            if num - 1 not in nums:
                count = 1
                current = num
                
                while current + 1 in nums:
                    count+=1
                    current+=1
                
                longest_count = max(longest_count, count)

        return longest_count
    

sol = Solution()
nums = [0,3,7,2,5,8,4,6,0,1]
print(sol.longestConsecutive(nums))

        