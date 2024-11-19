"""
You are given an integer array nums. A subsequence of nums is called a square streak if:

The length of the subsequence is at least 2, and
after sorting the subsequence, each element (except the first element) is the square of the previous number.
Return the length of the longest square streak in nums, or return -1 if there is no square streak.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: nums = [4,3,6,16,8,2]
Output: 3
Explanation: Choose the subsequence [4,16,2]. After sorting it, it becomes [2,4,16].
- 4 = 2 * 2.
- 16 = 4 * 4.
Therefore, [4,16,2] is a square streak.
It can be shown that every subsequence of length 4 is not a square streak.

Example 2:
Input: nums = [2,3,5,6,7]
Output: -1
Explanation: There is no square streak in nums so return -1.
"""
from typing import List
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # Convert nums list into set
        seen = set(nums)
        
        # keep track of the longest sequence of squares
        longest_count = 0

        # Iterate through each number in nums set
        for num in seen:
            
            # Avoid doing additional checking by making sure the num is the start of a sequence.
            # If num // num exists in the set, then num is not the start of the sequence.

            if num // num not in seen:
                
                # Start the count at 1, for the first number in the sequence
                count = 1  
                
                # Set the current power
                power = num ** 2

                # Iterate while num ** 2 is in the set
                while power in seen:

                    # Increase the count by one each time num * num is found
                    count += 1

                    # Raise the power (**2 becomes **4 becomes ** 8 etc)
                    power = power ** 2
                
                # Set longest_count to the count if it is the longest count seen yet.
                longest_count = max(longest_count, count)
                
        #Return the longest count if greater than 1. If not, return -1
        return longest_count if longest_count > 1 else -1
sol = Solution()

nums = [4,3,6,16,8,2]        
#nums = [2,3,5,6,7]
print(sol.longestSquareStreak(nums))