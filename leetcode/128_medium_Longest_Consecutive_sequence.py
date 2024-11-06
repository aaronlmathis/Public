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
        
        # keep track of the longest sequence
        longest_count = 0

        # Iterate through each number in nums set
        for num in nums:
            
            # Avoid doing additional checking by making sure the num is the start of a sequence.
            # If num - 1 exists in the set, then num is not the start of the sequence.
            if num - 1 not in nums:
                
                # Start the count at 1, for the first number in the sequence
                count = 1

                # Set the current number
                current = num
                
                # Iterate, checking to see if current number +1 is in the set, while it is, increase the count and current number by 1
                while current + 1 in nums:
                    count+=1
                    current+=1
                
                # Make longest_count equal to the count above if it is bigger than any previous count.
                longest_count = max(longest_count, count)
        
        # Return the longest count (longest sequence of numbers
        return longest_count
    

sol = Solution()
nums = [0,3,7,2,5,8,4,6,0,1]
print(sol.longestConsecutive(nums))

        